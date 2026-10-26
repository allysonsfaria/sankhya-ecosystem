---
id: "37773215468439"
titulo: "Como gerar e enviar o evento S1000"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37773215468439-Como-gerar-e-enviar-o-evento-S1000"
trilha: "Universidade Sankhya > Gestão eSocial"
atualizado_em: "2026-07-22T14:08:45Z"
rotulos: ["Configuração", "Eventos", "Pessoal", "eSocial", "Central do eSocial", "Sankhya"]
---

# Como gerar e enviar o evento S1000

| Categoria |
| --- |
| [O que é o evento S-1000?](https://ajuda.sankhya.com.br/hc/pt-br/articles/37773215468439-Como-gerar-e-enviar-o-evento-S1000#h_01KFB0T0EA1MGNTJDKY8BB2GN4) |
| [Vídeo de demonstração prática no sistema](https://ajuda.sankhya.com.br/hc/pt-br/articles/37773215468439-Como-gerar-e-enviar-o-evento-S1000#h_01KFB0SWNDMS38YHB2MRAMBYR0) |
| [É o momento de aplicar o conhecimento adquirido! Realize as movimentações no ERP Sankhya](https://ajuda.sankhya.com.br/hc/pt-br/articles/37773215468439-Como-gerar-e-enviar-o-evento-S1000#h_01KFB0SGJ289R1HDEMKQ8EJT8J) |
| [Correção e Repetição](https://ajuda.sankhya.com.br/hc/pt-br/articles/37773215468439-Como-gerar-e-enviar-o-evento-S1000#h_01KFB0RNHDDKP820G63R1P7PZJ) |

## Evento S1000 - Informações do empregador

#### O que é o evento S-1000?

O evento S-1000 é o ponto de partida do eSocial e o primeiro a ser transmitido ao Ambiente Nacional. Ele identifica o declarante (empresa ou órgão público), reunindo dados cadastrais, fiscais, alíquotas e enquadramentos. A partir desse evento, o sistema entende quem está enviando as informações e como os demais eventos devem ser validados e calculados, incluindo contribuições previdenciárias e FGTS.

No ERP Sankhya, dominar o S-1000 é essencial para garantir a conformidade legal e dar fluidez aos processos do Departamento Pessoal e SST.

##### Vídeo de demonstração prática no sistema

[Vídeo: tutorial do artigo](https://player.vimeo.com/video/1112989091)

#### É o momento de aplicar o conhecimento adquirido! Realize as movimentações no ERP Sankhya

Siga as orientações indicadas abaixo para executar o evento S1000 em sua base de testes.

1. **Conferência de dados básicos da empresa**

**Acesse**: Configurações » Cadastros » **Empresa**

- Localize o registro da empresa e verifique os campos:

**Aba Geral** 

- Razão Social
- CNPJ
- CPF do responsável
- Inscrição Estadual
- Produtor Rural - Campo marcado em cadastro de empresas deste segmento

**Aba Endereço**

- Todos os campos relativos à identificação completa do endereço da empresa devem estar preenchidos

**Aba Naturezas**

- Código do município
- Natureza do estabelecimento
- Natureza jurídica
- Atividade econômica
- Código de regime tributário
- E se os demais campos estão preenchidos com os dados correspondentes

**Aba Informações Fiscais**

- Verifique se os campos Cooperativa, Construtora e Classificação Tributária refletem corretamente a realidade da empresa

2. **Conferência do registro da empresa no módulo Pessoal**

**Acesse**: Configurações » Cadastros »  Pessoal » Empresas

- Localize o registro da empresa e verifique os campos:

**Aba Informações Gerais**

- Data de referência

**E-Social**

- O campo Grupo do eSocial deve estar preenchido de acordo com o enquadramento legal da empresa
- As datas de referência da Primeira, Segunda e Terceira Fase do eSocial devem estar devidamente informadas nos campos correspondentes

**Aba Informações Fiscais**

- O Indicativo Desoneração da Folha deve estar preenchido de acordo com a opção correta para a realidade da empresa

**Aba Geral**

- O Controle de ponto deve refletir o sistema adotado pela empresa

3. **Conferência do registro fiscal da empresa**

**Acesse**: Pessoal+  » Cadastros »  Registro Fiscal

Aba Geral

**PIS sobre a folha de pagamento**

- Preencha os campos Empresa Contribuinte, Alíquota e Código da Receita somente se houver incidência do imposto sobre a folha de pagamento

4. **Geração e envio do evento S1000**

**Acesse**: Pessoal+  » Rotinas Folha »  Central do eSocial

- Na lateral esquerda da tela, selecione a empresa, a referência e o ambiente de envio, e em seguida clique em **'Carregar'**.
- No menu lateral, acesse a aba “**Geração**” e escolha a opção individual
- Selecione o evento **S-1000** e em seguida clique em “**Iniciar** **Geração**”
- Após a geração, o evento será listado como card na aba **'Eventos Pendentes'**. Para realizar a transmissão ao eSocial, utilize o botão **'Enviar dados'**

Após o envio, o evento ficará na aba **'Eventos na Fila'** até a conclusão do processamento pelo ambiente do eSocial. Finalizado o envio, ele será movido para a aba '**Acompanhamento**', onde é possível visualizar os dados enviados e os XMLs de retorno por meio do botão **'Visualizar dados'**

#### Correção e Repetição

- Revise os registros para confirmar se os passos foram seguidos.
- Caso haja erro no registro verifique atentamente os campos mencionados no erro e consulte o manual do eSocial.
