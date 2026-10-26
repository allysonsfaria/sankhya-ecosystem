---
id: "44010828487703"
titulo: "Como posso otimizar as ligações via VoIP no sistema?"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44010828487703-Como-posso-otimizar-as-liga%C3%A7%C3%B5es-via-VoIP-no-sistema"
trilha: "Meetime > Ligações"
atualizado_em: "2026-10-05T18:47:36Z"
rotulos: ["sync_hc", "meetime", "meetime_445", "sync_hash_54b9b2f82c04"]
---

# Como posso otimizar as ligações via VoIP no sistema?

O VoIP (Voice over Internet Protocol) é um método que depende totalmente da conexão com a internet.

Para que os usuários tenham melhor qualidade nas ligações realizadas através da Meetime é possível fazer uma **priorização dos nossos IPs** na rede que você utiliza (configuração também chamada de QoS - Quality of Service).

Isso garante banda para quem fará as ligações. Seguem abaixo as instruções:

## Priorizar os IPs do intervalo abaixo (todo o tráfego TCP/UDP):

- 168.86.128.0 a 168.86.191.255 (CIDR 168.86.128.0/18) portas 1024 até 65535

**Cálculo de banda:** Para fazer o cálculo de banda que será priorizada considerar 100kbps por ligação simultânea. Por exemplo, se o time tem 8 pessoas ligando, priorizar 800kbps.

Obs.: os intervalos de IPs utilizados nas ligações feitas pela Meetime foram atualizados totalmente no dia 23/01/2024. Os antigos constam abaixo para consulta:

177.71.206.192 a 177.71.206.255 (CIDR 177.71.206.192/26) portas 1024 até 65535

18.228.249.0 a 18.228.249.255 (CIDR 18.228.249.0/24) portas 1024 até 65535

---

Ainda tem dúvidas? Entre em contato com a gente através do 
e-mail [suporte@meetime.com.br](mailto:suporte@meetime.com.br) ou WhatsApp através do número de telefone [(48) 3204-7590](https://wa.me/554832047590).
