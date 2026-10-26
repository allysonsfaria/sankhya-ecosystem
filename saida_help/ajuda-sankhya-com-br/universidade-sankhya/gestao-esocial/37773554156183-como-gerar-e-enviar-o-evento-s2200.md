---
id: "37773554156183"
titulo: "Como gerar e enviar o evento S2200"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37773554156183-Como-gerar-e-enviar-o-evento-S2200"
trilha: "Universidade Sankhya > Gestão eSocial"
atualizado_em: "2026-08-06T12:40:43Z"
rotulos: ["XML", "Admissão", "Pessoal", "eSocial", "Configuração Funcionários", "Central do eSocial"]
---

# Como gerar e enviar o evento S2200

| Categoria |
| --- |
| [O que é o evento S2200?](https://ajuda.sankhya.com.br/hc/pt-br/articles/37773554156183-Como-gerar-e-enviar-o-evento-S2200#h_01KFB284X7NK40TE5761GXZYS5) |
| [Vídeo de demonstração prática no sistema](https://ajuda.sankhya.com.br/hc/pt-br/articles/37773554156183-Como-gerar-e-enviar-o-evento-S2200#h_01KFB27W2VN69EKGB401MR8Q9V) |
| [Registro de admissão na tela Configuração Funcionários](https://ajuda.sankhya.com.br/hc/pt-br/articles/37773554156183-Como-gerar-e-enviar-o-evento-S2200#h_01KFB27G8NG48YJ3YRZ7VTCA2F) |
| [Geração e envio do evento S2200](https://ajuda.sankhya.com.br/hc/pt-br/articles/37773554156183-Como-gerar-e-enviar-o-evento-S2200#h_01KFB27791RT3NSSV660PEDTHS) |
| [Correção e Repetição](https://ajuda.sankhya.com.br/hc/pt-br/articles/37773554156183-Como-gerar-e-enviar-o-evento-S2200#h_01KFB26VTQWEMCDBJ485GTMJCN) |

## Evento S2200 - Cadastramento Inicial do Vínculo e Admissão do Trabalhador

#### O que é o evento S2200?

O evento S-2200 é utilizado para registrar a admissão completa de um trabalhador no eSocial, formalizando o início do vínculo empregatício. Ele contempla todas as informações obrigatórias sobre o colaborador, como dados cadastrais, tipo de contrato, cargo, salário, jornada, lotação tributária e demais elementos que caracterizam a relação de trabalho. 

Esse evento também é usado para o cadastramento inicial de vínculos ativos quando a empresa passa a adotar o eSocial, garantindo que todos os dados estejam atualizados e em conformidade com a legislação. A partir do S-2200, o sistema reconhece o trabalhador como parte da base do eSocial, permitindo o envio dos demais eventos relacionados à sua jornada, como folha de pagamento, afastamentos, férias e desligamento.

##### Vídeo de demonstração prática no sistema

[Vídeo: tutorial do artigo](https://player.vimeo.com/video/944171196)

#### É o momento de aplicar o conhecimento adquirido! Realize as movimentações no ERP Sankhya

1. ##### Registro de admissão na tela Configuração Funcionários

   **Acesse**: Configurações » Cadastros » Pessoal » Configurações Funcionários

- Aplique os filtros rápidos para localizar o registro dos funcionários e atente-se ao preenchimento dos seguintes dados:

  - CPF
  - Matrícula

Aba **Admissão**

- Código de categoria para o eSocial
- Vínculo
- Data de admissão
- Tipo de admissão
- Indicativo de admissão
- Situação eSocial

Aba **Endereço**

- Endereço do colaborador

Aba **Pessoais**

- Estado civil
- Naturalidade
- Nacionalidade
- Escolaridade
- Raça/Etnia
- Data de nascimento
- País de nascimento

Aba **Contrato**

- Campos referentes ao contrato de trabalho

Aba **Lotação**

- Preenchimento de campos obrigatórios - sinalizados com (\*) -.

2. ##### Geração e envio do evento S2200

**Acesse**: Pessoal+  » Rotinas Folha »  Central do eSocial

- Na lateral esquerda da tela, selecione a empresa, a referência e o ambiente de envio, e em seguida clique em '**Carregar**'.
- No menu lateral, acesse a aba “**Geração**” e escolha a opção **Individual**
- Selecione o evento **S-2200** e em seguida clique em “**Iniciar** **Geração**”
- Após a geração, o evento será listado como card na aba '**Eventos Pendentes**'. Para realizar a transmissão ao eSocial, utilize o botão '**Enviar dados**'

Após o envio, o evento ficará na aba '**Eventos na Fila**' até a conclusão do processamento pelo ambiente do eSocial. Finalizado o envio, ele será movido para a aba '**Acompanhamento**', onde é possível visualizar os dados enviados e os XMLs de retorno por meio do botão '**Visualizar dados**'

#### Correção e Repetição

- Revise os registros para confirmar se os passos foram seguidos.
- Caso haja erro no registro verifique atentamente os campos mencionados no erro e consulte o manual do eSocial.
