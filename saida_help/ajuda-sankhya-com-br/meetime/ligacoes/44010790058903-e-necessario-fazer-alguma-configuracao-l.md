---
id: "44010790058903"
titulo: "É necessário fazer alguma configuração/liberação na rede para ligar por VoIP?"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44010790058903-%C3%89-necess%C3%A1rio-fazer-alguma-configura%C3%A7%C3%A3o-libera%C3%A7%C3%A3o-na-rede-para-ligar-por-VoIP"
trilha: "Meetime > Ligações"
atualizado_em: "2026-10-05T18:45:41Z"
rotulos: ["sync_hc", "meetime", "sync_hash_a5deb5aa03c8", "meetime_444"]
---

# É necessário fazer alguma configuração/liberação na rede para ligar por VoIP?

Em uma ligação via VoIP o áudio trafega pela rede de Internet.

Caso você tenha na rede algum software/hardware que faça o controle de acesso a sites, será necessário verificar a provável liberação dos nossos endereços de IP.

Geralmente as empresas utilizam Firewall/Proxy para fazer esse tipo de controle, com isso, será necessário liberar todo o tráfego **TCP** e **UDP** para o intervalo de IPs:

- 168.86.128.0 a 168.86.191.255 (CIDR 168.86.128.0/18) portas 1024 até 65535

‼️Obs.: os intervalos de IPs utilizados nas ligações feitas pela Meetime foram atualizados totalmente no dia 23/01/2024. Os antigos constam abaixo para consulta:

177.71.206.192 a 177.71.206.255 (CIDR 177.71.206.192/26) portas 1024 até 65535

18.228.249.0 a 18.228.249.255 (CIDR 18.228.249.0/24) portas 1024 até 65535

---

Ainda tem dúvidas? Entre em contato com a gente através do 
e-mail [suporte@meetime.com.br](mailto:suporte@meetime.com.br) ou WhatsApp através do número de telefone [(48) 3204-7590](https://wa.me/554832047590).
