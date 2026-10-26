---
id: "44010361422871"
titulo: "Dificuldade para inicializar as ligações: como ajustar?"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44010361422871-Dificuldade-para-inicializar-as-liga%C3%A7%C3%B5es-como-ajustar"
trilha: "Meetime > Ligações"
atualizado_em: "2026-10-05T18:36:29Z"
rotulos: ["sync_hc", "meetime", "meetime_433", "sync_hash_ead4212aed0c"]
---

# Dificuldade para inicializar as ligações: como ajustar?

Para que uma chamada possa iniciar na Meetime, é necessário que ela conecte-se ao nosso servidor de VoIP.

Caso esse processo esteja demorando em várias ligações ou elas nem estejam iniciando, algum ponto relacionado à sua infra pode estar desajustado. Por favor, siga os passos abaixo para checagem:

1. Validar se você está utilizando o Google Chrome, navegador mais otimizado/recomendado para a tecnologia WebRTC (através da qual nossas ligações funcionam);
2. Fazer uma limpeza da memória do navegador apertando Ctrl + Shift + R (em qualquer tela da Meetime) para que qualquer inconsistência seja removida;
3. Verifique se o Chrome está atualizado: ícone de três pontinhos no canto superior direito do navegador > Ajuda > Sobre o Google Chrome;
4. Caso ele já esteja atualizado, tente reiniciá-lo (fechar todas as abas e abrir uma nova janela);
5. Em relação à rede de internet: verifique a possibilidade de utilizar um cabo de rede (se já estiver, tente desconectá-lo e conectá-lo mais uma vez ao computador) ou chegue mais próximo do modem e desative/ative o Wi-Fi;
6. Se o passo anterior não funcionar, tente reiniciar o modem;
7. Se possível, tente efetuar uma ligação conectado a outra rede de internet (pode ser o 4G do seu celular, por exemplo);
8. Por fim, tente reiniciar o computador.

## Bloqueios

Nesse caso, **nenhuma** chamada consegue ser efetuada através do sistema. Verifique se você utiliza algum proxy/firewall/antivírus que pode estar prejudicando a inicialização das ligações.

Você também pode realizar um teste para validar qualquer bloqueio clicando [aqui](https://networktest.twilio.com/?region=br1). Cada um dos 6 primeiros itens deverá retornar "Pass" ou "Fail", como ilustra o print abaixo:

![Imagem 1: Você também pode realizar um teste para validar qualquer bloqueio clicando aqui . Cada um dos 6 primeiros itens deverá…](https://ajuda.sankhya.com.br/hc/article_attachments/44010395005335)

Caso um desses itens retorne "Fail", provavelmente a rede de internet que você está utilizando possui bloqueios. É possível efetuar um teste em outra rede ou entrar em contato com o responsável pela TI e pedir a liberação conforme descrito neste artigo: [É necessário fazer alguma configuração/liberação na rede para ligar por VoIP?](https://cloudchat2.cloudhumans.com/hc/meetime/articles/1768846890-e-necessario-fazer-alguma-configuracao-liberacao-na-rede-para-ligar-por-vo_ip)

**Problema em nosso fornecedor que operacionaliza as chamadas**

Nesse cenário, o erro será observado por todos os usuários da Meetime (ou grande parte deles). Verifique nossa página de status ([aqui](https://status.meetime.com.br/)) para verificar se trata-se de uma instabilidade geral.

---

Ainda tem dúvidas? Entre em contato com a gente através do 
e-mail [suporte@meetime.com.br](mailto:suporte@meetime.com.br) ou WhatsApp através do número de telefone [(48) 3204-7590](https://wa.me/554832047590).
