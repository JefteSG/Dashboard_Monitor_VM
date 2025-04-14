import React, { useEffect, useState } from "react";
import { CheckCircle, XCircle, MoreHorizontal } from "lucide-react";
import { cn } from "@/lib/utils";
import {
  Card,
  CardContent,
  CardHeader,
  CardTitle,
} from "@/components/ui/card";
import { Progress } from "@/components/ui/progress";
import {
  DropdownMenu,
  DropdownMenuContent,
  DropdownMenuItem,
  DropdownMenuTrigger,
} from "@/components/ui/dropdown-menu";
import { Button } from "@/components/ui/button";
import {
  Dialog,
  DialogContent,
  DialogHeader,
  DialogTitle,
  DialogDescription,
  DialogFooter,
} from "@/components/ui/dialog";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";

interface VMCardProps {
  vmName: string;
  cpuUsage: number;
  ramUsage: number;
  diskUsage: number;
  online: boolean;
  ip: string;
  user: string;
  password: string;
  site: string;
}

export function VMCard({
  vmName,
  cpuUsage,
  ramUsage,
  diskUsage,
  online,
  ip,
  user,
  password,
  site,
}: VMCardProps) {
  const [cpu, setCpu] = useState(cpuUsage);
  const [ram, setRam] = useState(ramUsage);
  const [disk, setDisk] = useState(diskUsage);
  const [status, setStatus] = useState(online);

  const [editOpen, setEditOpen] = useState(false);
  const [editData, setEditData] = useState({ ip, user, password, site });
  
  // Atualiza estados internos quando as props mudam
  useEffect(() => setCpu(cpuUsage), [cpuUsage]);
  useEffect(() => setRam(ramUsage), [ramUsage]);
  useEffect(() => setDisk(diskUsage), [diskUsage]);
  useEffect(() => setStatus(online), [online]);

  const handleInputChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const { name, value } = e.target;
    console.log('handleInputChange',name, value);
    setEditData((prev) => ({ ...prev, [name]: value }));
  };
  const deleteCard = async () => {
    console.log("Remover VM:", vmName);
    await fetch(`/api/vm/${ip}`, {
      method: "DELETE",
      headers: {
        "Content-Type": "application/json",
      },
    });
  };
  const handleSave = () => {
    console.log("Dados salvos:", editData);
    setEditOpen(false);
  };

  return (
    <>
      <Card className={cn("w-[380px]")}>
        <CardHeader className="flex items-center justify-between">
          <CardTitle>{vmName}</CardTitle>
          <DropdownMenu>
            <DropdownMenuTrigger asChild>
              <Button
                variant="ghost" // Deixa o fundo transparente
                size="icon"     // Tamanho do botão reduzido para ícone
                className="h-8 w-8 p-0 flex items-center justify-center" // Ajuste de layout do botão
              >
                <MoreHorizontal className="h-4 w-4" />
              </Button>
            </DropdownMenuTrigger>
            <DropdownMenuContent align="end" className="w-48">
              <DropdownMenuItem onClick={() => setEditOpen(true)}>
                Editar
              </DropdownMenuItem>
              <DropdownMenuItem onClick={deleteCard}>
                Remover
              </DropdownMenuItem>
            </DropdownMenuContent>
          </DropdownMenu>
        </CardHeader>
        <CardContent className="space-y-4">
          <div>
            <p className="text-sm font-medium">Uso de CPU</p>
            <Progress value={cpu} className="h-2" />
            <p className="text-xs text-muted-foreground">{cpu}%</p>
          </div>
          <div>
            <p className="text-sm font-medium">Uso de RAM</p>
            <Progress value={ram} className="h-2" />
            <p className="text-xs text-muted-foreground">{ram}%</p>
          </div>
          <div>
            <p className="text-sm font-medium">Uso de Disco</p>
            <Progress value={disk} className="h-2" />
            <p className="text-xs text-muted-foreground">{disk}%</p>
          </div>
          <div className="flex items-center space-x-2">
            <p className="text-sm font-medium">Status</p>
            {status ? (
              <CheckCircle className="text-green-500" size={20} />
            ) : (
              <XCircle className="text-red-500" size={20} />
            )}
            <p className="text-sm">{status ? "Online" : "Offline"}</p>
          </div>
        </CardContent>
      </Card>

      {/* Modal de Edição */}
      <Dialog open={editOpen} onOpenChange={setEditOpen}>
        <DialogContent>
          <DialogHeader>
            <DialogTitle>Editar VM - {vmName}</DialogTitle>
            <DialogDescription>
              Altere as configurações da sua VM.
            </DialogDescription>
          </DialogHeader>
          <div className="space-y-4">
            <div>
              <Label htmlFor="ip">IP</Label>
              <Input
                id="ip"
                name="ip"
                value={editData.ip}
                onChange={handleInputChange}
              />
            </div>
            <div>
              <Label htmlFor="user">Usuário</Label>
              <Input
                id="user"
                name="user"
                value={editData.user}
                onChange={handleInputChange}
              />
            </div>
            <div>
              <Label htmlFor="password">Senha</Label>
              <Input
                id="password"
                name="password"
                type="password"
                value={editData.password}
                onChange={handleInputChange}
              />
            </div>
            <div>
              <Label htmlFor="site">Site</Label>
              <Input
                id="site"
                name="site"
                value={editData.site}
                onChange={handleInputChange}
              />
            </div>
          </div>
          <DialogFooter>
            <Button variant="ghost" onClick={() => setEditOpen(false)}>
              Cancelar
            </Button>
            <Button onClick={handleSave}>Salvar</Button>
          </DialogFooter>
        </DialogContent>
      </Dialog>
    </>
  );
}
