// components/ui/AddVM.tsx
import React, { useState } from "react";
import { Button } from "@/components/ui/button";
import {
  Dialog,
  DialogContent,
  DialogHeader,
  DialogTitle,
  DialogFooter,
  DialogTrigger,
} from "@/components/ui/dialog";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";

// Interface para os dados da VM que são configuráveis pelo usuário
export interface NewVMData {
  name: string;
  ip_address: string;
  username: string;
  password: string;
  site_url: string;
}

interface AddVMProps {
  onAdd: (vm: NewVMData) => void;
}

export function AddVM({ onAdd }: AddVMProps) {
  const [open, setOpen] = useState(false);
  const [newVm, setNewVm] = useState<NewVMData>({
    name: "",
    ip_address: "",
    username: "",
    password: "",
    site_url: "",
  });

  const handleInputChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const { name, value, type } = e.target;
    setNewVm((prev) => ({
      ...prev,
      [name]: type === "number" ? Number(value) : value,
    }));
  };

  const handleSubmit = async (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    onAdd(newVm);
    // Reseta o formulário e fecha o modal
    setNewVm({
      name: "",
      ip_address: "",
      username: "",
      password: "",
      site_url: "",
    });
    setOpen(false);
  };

  return (
    <Dialog open={open} onOpenChange={setOpen}>
      <DialogTrigger asChild>
        <Button>Adicionar Nova VM</Button>
      </DialogTrigger>
      <DialogContent>
        <DialogHeader>
          <DialogTitle>Adicionar Nova VM</DialogTitle>
        </DialogHeader>
        <form onSubmit={handleSubmit} className="space-y-4">
          <div>
            <Label htmlFor="name">Nome da VM</Label>
            <Input
              id="name"
              name="name"
              value={newVm.name}
              onChange={handleInputChange}
              placeholder="VM Exemplo"
            />
          </div>
          <div>
            <Label htmlFor="ip_address">IP</Label>
            <Input
              id="ip_address"
              name="ip_address"
              value={newVm.ip_address}
              onChange={handleInputChange}
              placeholder="192.168.0.1"
            />
          </div>
          <div>
            <Label htmlFor="username">Usuário</Label>
            <Input
              id="username"
              name="username"
              value={newVm.username}
              onChange={handleInputChange}
              placeholder="root"
            />
          </div>
          <div>
            <Label htmlFor="password">Senha</Label>
            <Input
              id="password"
              name="password"
              type="password"
              value={newVm.password}
              onChange={handleInputChange}
              placeholder="********"
            />
          </div>
          <div>
            <Label htmlFor="site_url">Site</Label>
            <Input
              id="site_url"
              name="site_url"
              value={newVm.site_url}
              onChange={handleInputChange}
              placeholder="https://www.example.com"
            />
          </div>
          <DialogFooter>
            <Button type="submit">Salvar</Button>
          </DialogFooter>
        </form>
      </DialogContent>
    </Dialog>
  );
}
