---
id: "44010421069591"
titulo: "Erro de conexão com o servidor: como resolver?"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44010421069591-Erro-de-conex%C3%A3o-com-o-servidor-como-resolver"
trilha: "Meetime > Ligações"
atualizado_em: "2026-10-05T18:37:27Z"
rotulos: ["sync_hc", "meetime", "meetime_434", "sync_hash_380c0c3f670e"]
---

# Erro de conexão com o servidor: como resolver?

Caso você esteja observando um aviso que indica esse erro, suas ligações feitas através da Meetime estão sendo impactadas. Elas podem não conseguir inicializar ou até mesmo cair durante a chamada. Colocamos abaixo os motivos pelos quais esse erro pode acontecer e como ajustar a situação:

## 1. Bloqueio de rede

Nesse caso, **nenhuma** chamada consegue ser efetuada através do sistema. Para validar se realmente trata-se de bloqueio, você pode realizar um teste clicando [aqui](https://networktest.twilio.com/?region=br1).

Cada um dos 6 primeiros itens deverá retornar "Pass" ou "Fail", como ilustra o print abaixo:

![Imagem 1: Cada um dos 6 primeiros itens deverá retornar "Pass" ou "Fail", como ilustra o print abaixo:](https://suporte.meetime.com.br/hc/article_attachments/360088583234/Teste_Twilio_-_print.png)

Caso um dos itens retorne "Fail", provavelmente a rede de internet que você está utilizando possui bloqueios. É possível efetuar um teste em outra rede ou entrar em contato com o responsável pela TI e pedir a liberação conforme descrito neste artigo: [É necessário fazer alguma configuração/liberação na rede para ligar por VoIP?](https://cloudchat2.cloudhumans.com/hc/meetime/articles/1768846890-e-necessario-fazer-alguma-configuracao-liberacao-na-rede-para-ligar-por-vo_ip)

## 2. Navegador inadequado/Rede insuficiente

Alguns pontos de infra podem estar causando o erro. Por favor, siga os passos abaixo para checagem:

- Validar se você está utilizando o Google Chrome, navegador mais otimizado/recomendado para a tecnologia WebRTC (através da qual nossas ligações funcionam);
- Se você estiver usando o Chrome, tente reiniciá-lo (fechar todas as abas e abrir uma nova janela);
- Em relação à rede de internet: verifique a possibilidade de utilizar um cabo de rede (se já estiver, tente desconectá-lo e conectá-lo mais uma vez ao computador) ou chegue mais próximo do modem e desative/ative o Wi-Fi;
- Se o passo anterior não funcionar, tente reiniciar o modem;
- Se possível, tente efetuar uma ligação conectado a outra rede de internet (pode ser o 4G do seu celular, por exemplo);
- Por fim, tente reiniciar o computador.

## 3. Problema em nosso fornecedor que operacionaliza as chamadas

Nesse cenário, o erro será observado por todos os usuários da Meetime (ou grande parte deles). Verifique nossa página de status ([aqui](https://status.meetime.com.br/)) para verificar se trata-se de uma instabilidade geral.

---

Ainda tem dúvidas? Entre em contato com a gente através do 
e-mail [suporte@meetime.com.br](mailto:suporte@meetime.com.br) ou WhatsApp através do número de telefone [(48) 3204-7590](https://wa.me/554832047590).
