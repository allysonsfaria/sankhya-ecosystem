---
id: "37773277986839"
titulo: "Como gerar e enviar o evento S1005"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37773277986839-Como-gerar-e-enviar-o-evento-S1005"
trilha: "Universidade Sankhya > Gestão eSocial"
atualizado_em: "2026-07-22T14:08:44Z"
rotulos: ["Configuração", "Eventos", "Pessoal", "eSocial", "Central do eSocial"]
---

# Como gerar e enviar o evento S1005

| Categoria |
| --- |
| [O que é o evento S-1005?](https://ajuda.sankhya.com.br/hc/pt-br/articles/37773277986839-Como-gerar-e-enviar-o-evento-S1005#h_01KFB15Y2FY209YZVMCVK5CR53) |
| [Vídeo de demonstração prática no sistema](https://ajuda.sankhya.com.br/hc/pt-br/articles/37773277986839-Como-gerar-e-enviar-o-evento-S1005#h_01KFB15SWBSXT8E3TFYEKFMSYS) |
| [Conferência de dados básicos da empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/37773277986839-Como-gerar-e-enviar-o-evento-S1005#h_01KFB15D5G405T8H1HBP7R1TZC) |
| [Conferência do registro fiscal da empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/37773277986839-Como-gerar-e-enviar-o-evento-S1005#h_01KFB158XWR06CN6SJP1ZX3420) |
| [Conferência do registro da empresa no módulo Pessoal](https://ajuda.sankhya.com.br/hc/pt-br/articles/37773277986839-Como-gerar-e-enviar-o-evento-S1005#h_01KFB153CNFNE9342H4Y8YN39N) |
| [Geração e envio do evento S1005](https://ajuda.sankhya.com.br/hc/pt-br/articles/37773277986839-Como-gerar-e-enviar-o-evento-S1005#h_01KFB14W5WRGGNCG1FTH8Z1K7C) |
| [Correção e Repetição](https://ajuda.sankhya.com.br/hc/pt-br/articles/37773277986839-Como-gerar-e-enviar-o-evento-S1005#h_01KFB14E6PPGCSK3E7G3QJG0DQ) |

## Evento S1005 - Estabelecimentos

#### O que é o evento S-1005?

O evento S-1005 é responsável por registrar no eSocial os dados cadastrais de cada estabelecimento da empresa, obras ou unidades administrativas. Ele identifica o CNPJ completo de cada local e leva informações essenciais como CNAE preponderante, alíquota do RAT, FAP, indicações sobre contratação de PCD e outros dados importantes para o cálculo correto de encargos como FGTS e INSS. Além disso, o S-1005 informa se a unidade é uma obra própria ou por empreitada, se há processo judicial vinculado à empresa, e traz os dados de contato da unidade.  Esse evento garante que a apuração dos encargos trabalhistas e previdenciários esteja alinhada à realidade de cada local de operação da empresa.

##### Vídeo de demonstração prática no sistema

[Vídeo: tutorial do artigo](https://player.vimeo.com/video/1114361145)

#### É o momento de aplicar o conhecimento adquirido! Realize as movimentações no ERP Sankhya

Siga as orientações indicadas abaixo para executar o evento S1005 em sua base de testes.

1. ##### Conferência de dados básicos da empresa

**Acesse**: Configurações » Cadastros » **Empresa**

- Localize o registro da empresa e verifique, na aba Naturezas, se o campo CNAE Preponderante está devidamente preenchido conforme a atividade principal da empresa

2. ##### Conferência do registro fiscal da empresa

**Acesse**: Pessoal+  » Cadastros »  Registro Fiscal

- Validar se o campo Taxa de Seguro está corretamente preenchido com a Alíquota RAT aplicável ao estabelecimento
- Confirmar se o campo Fator Acidentário de Prevenção (FAP) está informado conforme o índice vigente para a empresa
- Verificar se o campo CNAE/IBGE está preenchido de acordo com a Classificação Nacional da Atividade Econômica da unidade
- Certificar-se de que a seção de Inscrição está devidamente preenchida conforme o tipo de estabelecimento (CNPJ, CNO, CAEPF, etc.)

3. ##### Conferência do registro da empresa no módulo Pessoal

**Acesse**: Configurações » Cadastros »  Pessoal » Empresas

- Certifique-se de que o campo 'Contratação de PCD' está devidamente preenchido conforme a política de inclusão adotada pela empresa
- Valide se o campo 'Contratação de Aprendiz' está informado de acordo com a obrigatoriedade legal aplicável ao estabelecimento

4. ##### Geração e envio do evento S1005

**Acesse**: Pessoal+  » Rotinas Folha »  Central do eSocial

- Na lateral esquerda da tela, selecione a empresa, a referência e o ambiente de envio, e em seguida clique em **'Carregar'**.
- No menu lateral, acesse a aba “**Geração**” e escolha a opção **Individual**
- Selecione o evento **S-1005** e em seguida clique em “**Iniciar** **Geração**”
- Após a geração, o evento será listado como card na aba '**Eventos Pendentes**'. Para realizar a transmissão ao eSocial, utilize o botão '**Enviar dados**'

Após o envio, o evento ficará na aba '**Eventos na Fila**' até a conclusão do processamento pelo ambiente do eSocial. Finalizado o envio, ele será movido para a aba '**Acompanhamento**', onde é possível visualizar os dados enviados e os XMLs de retorno por meio do botão **'Visualizar dados'**

#### Correção e Repetição

- Revise os registros para confirmar se os passos foram seguidos.
- Caso haja erro no registro verifique atentamente os campos mencionados no erro e consulte o manual do eSocial.
