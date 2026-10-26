---
id: "44010872085143"
titulo: "Requisitos para realizar ligações com qualidade"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44010872085143-Requisitos-para-realizar-liga%C3%A7%C3%B5es-com-qualidade"
trilha: "Meetime > Ligações"
atualizado_em: "2026-10-05T18:49:08Z"
rotulos: ["sync_hc", "meetime", "meetime_447", "sync_hash_2ea2fe1c0684"]
---

# Requisitos para realizar ligações com qualidade

## Conexão com a internet

As ligações realizadas via VoIP dependem 100% da conexão com a internet, por isso o mais importante para a qualidade das ligações é conexão boa e estável.

O uso de um **cabo de rede** em seu computador é altamente recomendado para evitar interferências causadas via Wi-fi.

Muitos usuários utilizam a conexão via Wi-fi devido a praticidade, mas por ser uma rede sem fio o recebimento de sinal não se mantém estável. Um exemplo desse comportamento é o uso de fones com fio e sem fio, onde o fone sem fio apresenta falhas no áudio com maior frequência do que o fone cabeado. Isso ocorre, pois a conexão via cabo faz o contato direto entre um dispositivo e outro, sem interferências no caminho!

Caso seu computador não tenha entrada de rede existem vários tipos de adaptadores USB como o exemplo abaixo:

![Imagem 1: Caso seu computador não tenha entrada de rede existem vários tipos de adaptadores USB como o exemplo abaixo:](https://suporte.meetime.com.br/hc/article_attachments/17748682148121)

**Importante:** o wi-fi precisa estar desativado para o computador utilizar apenas a conexão cabeada.

Caso utilize software na rede que faça o controle de acesso a sites, será necessário verificar a liberação dos endereços de IP utilizados para realizar as ligações.

Geralmente as empresas utilizam Firewall/Proxy para fazer esse tipo de controle, com isso, será necessário liberar todo o tráfego TCP e UDP para os intervalos de IPs:

```
168.86.128.0 a 168.86.191.255 (CIDR 168.86.128.0/18) portas 1024 até 65535
```

## Áudio

Além da internet, o fone utilizado também afeta a desempenho das suas chamadas. Por isso recomendamos o uso de fones específicos para ligações que utilizem entrada USB. Esse tipo de fone é projetado para ligações, com um desempenho maior na captação e reprodução de áudio, assegurando que o lead te escute de forma nítida.

![Imagem 2: Além da internet, o fone utilizado também afeta a desempenho das suas chamadas. Por isso recomendamos o uso de fones…](https://suporte.meetime.com.br/hc/article_attachments/17748681226649)

Para garantir que as configurações do fone estão corretas, verifique os pontos citados em nosso artigo: [Configurações de áudio](https://cloudchat2.cloudhumans.com/hc/meetime/articles/1768855788-a-ligacao-via-voi_p-inicia-mas-eu-nao-consigo-escutar-a-outra-pessoa-como-posso-corrigir-isso)

---

Ainda tem dúvidas? Entre em contato com a gente através do 
e-mail [suporte@meetime.com.br](mailto:suporte@meetime.com.br) ou WhatsApp através do número de telefone [(48) 3204-7590](https://wa.me/554832047590).
