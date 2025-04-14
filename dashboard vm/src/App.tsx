import { useEffect, useState } from "react";
import { VMCard } from "./components/ui/card_dash";
import { AddVM, NewVMData } from "./components/ui/AddVM";
import "./App.css";

interface VMData {
  vm_name: string;
  cpu_usage: number;
  ram_usage: number;
  disk_usage: number;
  site_status: boolean;
  ssh_status: boolean;
  ip: string;
  user: string;
  password: string;
  site: string;
}

function App() {
  const [vmCards, setVmCards] = useState<VMData[]>([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const ws = new WebSocket("ws://localhost:8000/ws/monitor");

    ws.onmessage = (event) => {
      try {
        const response = JSON.parse(event.data);
        if (!Array.isArray(response)) {
          console.warn("Dados recebidos não estão no formato esperado:", response);
          return;
        }
        const newData = response as VMData[];

        setVmCards((prevCards) => {
          const updatedCards = [...prevCards];

          newData.forEach((newVm) => {
            const existingIndex = updatedCards.findIndex(vm => vm.vm_name === newVm.vm_name);
            if (existingIndex !== -1) {
              updatedCards[existingIndex] = { ...updatedCards[existingIndex], ...newVm };
            } else {
              updatedCards.push(newVm);
            }
          });

          return updatedCards;
        });

        setLoading(false);
      } catch (err) {
        console.error("Erro ao processar mensagem do WebSocket:", err);
      }
    };

    ws.onerror = (err) => console.error("Erro no WebSocket:", err);
    ws.onclose = () => console.log("WebSocket desconectado");

    return () => {
      ws.close();
    };
  }, []);

  const handleAddVm = async (newVm: NewVMData) => {
    try {
      const response = await fetch("/api/vm", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(newVm),
      });
      if (!response.ok) throw new Error("Erro ao adicionar VM");
    } catch (error) {
      console.error("Erro ao adicionar VM:", error);
    }
  };

  return (
    <div className="App container mx-auto p-4">
      {/* Header fixo com título e botão */}
      <div className="sticky top-0 z-10 bg-white pb-4 mb-6 flex justify-between items-center border-b border-gray-200">
        <h1 className="text-2xl font-bold">Dashboard de VMs</h1>
        <AddVM onAdd={handleAddVm} />
      </div>
  
      {/* Grid de VMs ou Skeleton */}
      <div className="grid gap-4 mb-8 grid-cols-2">
        {loading ? (
          // Mostra esqueleto de loading enquanto carrega
          [...Array(2)].map((_, index) => (
            <div
              key={index}
              className="p-4 rounded-xl shadow-md bg-gray-100 animate-pulse h-40"
            />
          ))
        ) : (
          // Mostra os cards reais
          vmCards.map((vm) => (
            <VMCard
              key={vm.ip}
              vmName={vm.vm_name}
              cpuUsage={vm.cpu_usage}
              ramUsage={vm.ram_usage}
              diskUsage={vm.disk_usage}
              online={vm.site_status}
              ip={vm.ip}
              user={vm.user}
              password={vm.password}
              site={vm.site}
            />
          ))
        )}
      </div>
    </div>
  );  
}

export default App;
