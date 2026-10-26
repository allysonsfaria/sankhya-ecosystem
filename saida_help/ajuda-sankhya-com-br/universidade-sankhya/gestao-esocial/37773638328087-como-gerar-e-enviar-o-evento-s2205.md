---
id: "37773638328087"
titulo: "Como gerar e enviar o evento S2205"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37773638328087-Como-gerar-e-enviar-o-evento-S2205"
trilha: "Universidade Sankhya > Gestão eSocial"
atualizado_em: "2026-07-22T14:08:39Z"
rotulos: ["Eventos", "Funcionários", "XML", "eSocial", "Central do eSocial", "Cadastro"]
---

# Como gerar e enviar o evento S2205

| Categoria |
| --- |
| [O que é o evento S2205](https://ajuda.sankhya.com.br/hc/pt-br/articles/37773638328087-Como-gerar-e-enviar-o-evento-S2205#h_01KFB2GFRPC84X8HSVM0E66SMC) |
| [Vídeo de demonstração prática no sistema](https://ajuda.sankhya.com.br/hc/pt-br/articles/37773638328087-Como-gerar-e-enviar-o-evento-S2205#h_01KFB2GBQEPMJD6A5EBAT5WCST) |
| [Para alterações de cadastros](https://ajuda.sankhya.com.br/hc/pt-br/articles/37773638328087-Como-gerar-e-enviar-o-evento-S2205#h_01KFB2FT8CANKEG2D98C049M04) |
| [Geração e envio do evento S2205](https://ajuda.sankhya.com.br/hc/pt-br/articles/37773638328087-Como-gerar-e-enviar-o-evento-S2205#h_01KFB2FK1FWYPA33GPQ5N065F1) |
| [Correção e Repetição](https://ajuda.sankhya.com.br/hc/pt-br/articles/37773638328087-Como-gerar-e-enviar-o-evento-S2205#h_01KFB2F6X9SPDJDQ7CK626NHYG) |

## Evento S2205 - Alteração de Dados Cadastrais do Trabalhador

#### O que é o evento S2205?

O evento S-2205 é utilizado para comunicar ao eSocial qualquer alteração nos dados cadastrais do trabalhador, como nome, CPF, NIS, estado civil, grau de instrução, data de nascimento ou nacionalidade. Esse evento não altera as condições contratuais do vínculo de trabalho, ele apenas atualiza as informações pessoais previamente enviadas no evento S-2200 (Admissão) ou no S-2300 (Trabalhador sem vínculo). Sempre que houver esse tipo de modificação, o envio do S-2205 é obrigatório para manter o cadastro do trabalhador atualizado e alinhado com os registros oficiais, garantindo a consistência das informações transmitidas ao eSocial.

##### Vídeo de demonstração prática no sistema

[Vídeo: tutorial do artigo](https://player.vimeo.com/video/944170974)

#### É o momento de aplicar o conhecimento adquirido! Realize as movimentações no ERP Sankhya

1. ##### Para alterações de cadastros

**Acesse**: Configurações » Cadastros » Pessoal » Configurações Funcionários

- Para que as alterações sejam geradas, é importante ressaltar que o camo Situação eSocial precisa estar alimentado com uma das seguintes opções: Oficial, e S-2205 ou Oficial, S22-05, S2206 e S2306. Após a admissão, assim que é transmitido as informações da primeira folha do funcionário e enviados os eventos periodicos S1200 e S1210 quando a empresa finalizar a competência enviando o evento S1299 um job (serviço) será executado e fará a alteração desse campo de forma automática no cadastro dos funcionários, logo, não é necessário se preocupar em fazer essa alteração de forma manual, em nosso vídeo, para fins didáticos foi demonstrado como fazer a alteração do campo porém esse processo será feito de forma automática após a finalização da primeira folha de pagamento do funcionário.
- Após realizar as alterações no cadastro do usuário é necessário preencher a data de alteração e descrição opcional dos dados modificados.

2. ##### Geração e envio do evento S2205

**Acesse**: Pessoal+  » Rotinas Folha »  Central do eSocial

- Na lateral esquerda da tela, selecione a empresa, a referência e o ambiente de envio, e em seguida clique em '**Carregar**'.
- No menu lateral, acesse a aba “**Geração**” e escolha a opção **Individual**
- Selecione o evento **S-2205** e em seguida clique em “**Iniciar** **Geração**”
- Após a geração, o evento será listado como card na aba '**Eventos Pendentes**'. Para realizar a transmissão ao eSocial, utilize o botão '**Enviar dados**'

Após o envio, o evento ficará na aba '**Eventos na Fila**' até a conclusão do processamento pelo ambiente do eSocial. Finalizado o envio, ele será movido para a aba '**Acompanhamento**', onde é possível visualizar os dados enviados e os XMLs de retorno por meio do botão '**Visualizar dados**'

#### Correção e Repetição

- Revise os registros para confirmar se os passos foram seguidos.
- Caso haja erro no registro verifique atentamente os campos mencionados no erro e consulte o manual do eSocial.
