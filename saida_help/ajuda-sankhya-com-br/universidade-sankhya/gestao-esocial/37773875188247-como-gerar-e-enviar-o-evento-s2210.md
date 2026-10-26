---
id: "37773875188247"
titulo: "Como gerar e enviar o evento S2210"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37773875188247-Como-gerar-e-enviar-o-evento-S2210"
trilha: "Universidade Sankhya > Gestão eSocial"
atualizado_em: "2026-07-26T12:36:46Z"
rotulos: ["SST", "eSocial", "Central do eSocial", "CAT", "Pessoal+"]
---

# Como gerar e enviar o evento S2210

| Categoria |
| --- |
| [O que é o evento S2210?](https://ajuda.sankhya.com.br/hc/pt-br/articles/37773875188247-Como-gerar-e-enviar-o-evento-S2210#h_01KFB382AKJSAF5E60ABSCR4AN) |
| [Vídeo com demonstração prática no sistema](https://ajuda.sankhya.com.br/hc/pt-br/articles/37773875188247-Como-gerar-e-enviar-o-evento-S2210#h_01KFB35N94ZH06CVZ98PT3X8XW) |
| [Para lançar a Comunicação de Acidente de Trabalho (CAT)](https://ajuda.sankhya.com.br/hc/pt-br/articles/37773875188247-Como-gerar-e-enviar-o-evento-S2210#h_01KFB35AYFWSAG8F9YAQ722EZE) |
| [Geração e envio do evento S2210](https://ajuda.sankhya.com.br/hc/pt-br/articles/37773875188247-Como-gerar-e-enviar-o-evento-S2210#h_01KFB354S9QFCBXACASAZH55AG) |
| [Correção e Repetição](https://ajuda.sankhya.com.br/hc/pt-br/articles/37773875188247-Como-gerar-e-enviar-o-evento-S2210#h_01KFB34Q0ZZEKQZAYJ796SC55Z) |

## Evento S2210 - Comunicação de Acidente de Trabalho (CAT)

#### O que é o evento S2210?

O evento S-2210 é utilizado para comunicar ao eSocial a ocorrência de acidente de trabalho, seja típico (no exercício da função) ou de trajeto (entre residência e local de trabalho), envolvendo um colaborador. Esse evento substitui a Comunicação de Acidente de Trabalho (CAT) em papel e deve ser transmitido até o primeiro dia útil subsequente à ocorrência ou imediatamente, em caso de óbito. Ele faz parte do grupo de eventos de Saúde e Segurança do Trabalho (SST) e tem como objetivo registrar formalmente o acidente, garantindo os direitos previdenciários do trabalhador junto ao INSS e comprovando o cumprimento da obrigação legal por parte da empresa, mesmo quando o acidente não resulta em afastamento.

##### Vídeo com demonstração prática no sistema

[Vídeo: tutorial do artigo](https://player.vimeo.com/video/944191324)

#### É o momento de aplicar o conhecimento adquirido! Realize as movimentações no ERP Sankhya

1. ##### Para lançar a Comunicação de Acidente de Trabalho (CAT)

**Acesse**: Pessoal+ » Rotinas Folha » SESMT » CAT - Comunicação de Acidente de Trabalho

- Faça a inclusão do registro informando a empresa e o funcionário

**Aba Geral**

- Preencha o campo Tipo de CAT
- Tipo de acidente
- Iniciativa da CAT
- Data do acidente
- Hora do acidente
- Horas trabalhadas
- Último dia trabalhado
- Situação Geradora do Acidente

**Aba Local do Acidente**

- Tipo de local
- CEP
- Endereço
- Bairro
- Cidade

**Aba Atestado médico**

- Data de atendimento
- Hora atendimento
- Duração do tratamento (em dias)
- Descrição da lesão
- CID
- Médico
- Inscrição no órgão de classe
- Órgão de classe
- UF órgão de classe

**Aba Partes do corpo atingidas**

- Inclua o código da parte do corpo buscando pela lupa
- Preencha a Lateralidade indicando o lado da parte do corpo atingida

2. ##### Geração e envio do evento S2210

**Acesse**: Pessoal+  » Rotinas Folha »  Central do eSocial

- Na lateral esquerda da tela, selecione a empresa, a referência e o ambiente de envio, e em seguida clique em '**Carregar**'.
- No menu lateral, acesse a aba “**Geração**” e escolha a opção **Individual**
- Selecione o evento **S-2210** e em seguida clique em “**Iniciar** **Geração**”
- Após a geração, o evento será listado como card na aba '**Eventos Pendentes**'. Para realizar a transmissão ao eSocial, utilize o botão '**Enviar dados**'

Após o envio, o evento ficará na aba '**Eventos na Fila**' até a conclusão do processamento pelo ambiente do eSocial. Finalizado o envio, ele será movido para a aba '**Acompanhamento**', onde é possível visualizar os dados enviados e os XMLs de retorno por meio do botão '**Visualizar dados**'

#### Correção e Repetição

- Revise os registros para confirmar se os passos foram seguidos.
- Caso haja erro no registro verifique atentamente os campos mencionados no erro e consulte o manual do eSocial.
