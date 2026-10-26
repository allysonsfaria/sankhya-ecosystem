---
id: "360044579914"
titulo: "Melhores Práticas para Emissão de 'MDF-e - Manifesto de Documento Fiscal Eletrônico'."
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044579914-Melhores-Pr%C3%A1ticas-para-Emiss%C3%A3o-de-MDF-e-Manifesto-de-Documento-Fiscal-Eletr%C3%B4nico"
trilha: "Melhores Práticas > Vendas"
atualizado_em: "2026-07-22T15:51:25Z"
rotulos: ["DUVIDAMDFE", "MDF-e", "Configuração", "XML", "SEFAZ", "Transporte", "Criação de OC e CT-e vinculação e configuração de viagem", "Configurações de embarcação criação e encerramento de MDF-e", "Documento digital vincula notas sem impostos não gera SPED", "Documentos Eletrônicos"]
---

# Melhores Práticas para Emissão de 'MDF-e - Manifesto de Documento Fiscal Eletrônico'.

**Manifesto Eletrônico de Documentos Fiscais (MDF-e)** é o documento emitido e armazenado eletronicamente, de existência apenas digital, para vincular os documentos fiscais transportados na unidade de carga utilizada, cuja validade jurídica é garantida pela assinatura digital do emitente e autorização de uso pelo Ambiente Autorizador.

O MDF-e serve para consolidar em um único documento todas as NF-es e CT-es que compõem a viagem, permitindo o rastreamento da carga e do veículo pelos órgãos da SEFAZ e ANTT. Ele identifica o responsável pelo transporte, agiliza o registro em lote dos documentos fiscais e facilita a conferência e fiscalização em barreiras. Além disso, o MDF-e registra alterações de condutores, unidades de transporte ou de carga, garantindo maior controle e reduzindo riscos de multas ou retenção do veículo.

#### Quem deve emitir o MDF-e?

A emissão do MDF-e é obrigatória em todo o território nacional, conforme especificado pelo Ajuste SINEEF 21/2010  sendo de responsabilidade das empresas de transporte de cargas e mercadorias. Para uma empresa emitir o MDF-e ela necessita de se credenciar junto à Secretaria da Fazenda, como emissora de CTe ou NFe, Adquirir um Certificado Digital para validar juridicamente o MDFe e conter um software que emita o MDF-e.

#### Premissas do uso da MDF-e:

- Registro RNTRC (Configurações » Cadastros » Empresas, aba: Natureza), caso Modal Rodoviário
- Versão MDF-e= **Versão MDF-e 3.00**(Comercial » Preferências » Empresa, aba: MDF-e)
- MDF-e é um Documento que não tem incidência de Impostos.
- MDF-e não exige configuração de TOP.
- MDF-e não gera informações para SPED Fiscal/Contribuições.
- Quando existir 2 entregas, uma para dentro do estado e outra para fora, será emitido 2(duas) MDF-e.

#### Onde emitir um MDF-e no Sankhya?

- Acesse [''**Ordens de Carga''**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045119713-Ordens-de-Carga) (Comercial » Rotinas » Ordem de Carga » Ordens de Carga) e clique em ''**Criar Viagem''**.
- Crie uma OC (Ordem de Carga), que será vinculada à NF-e ou CT-e aprovado.
- O sistema abrirá a rotina [**''Viagens de Transporte (MDF-e)''**](https://ajuda.sankhya.com.br/hc/pt-br/articles/Comercial%20%C2%BB%20Rotinas%20%C2%BB%20Viagens%20de%20Transporte%20(MDF-e)) para complementação das informações.
- Também é possível fazer o lançamento manual diretamente na rotina.
- A transmissão para a SEFAZ e demais ações (eventos, XML, contingência, encerramento) ocorrem nesta mesma tela.

![Imagem 1: A transmissão para a SEFAZ e demais ações (eventos, XML, contingência, encerramento) ocorrem nesta mesma tela.](https://ajuda.sankhya.com.br/hc/article_attachments/37027273299991)

#### Como efetuar o lançamento de uma MDF-e:

**1. Modal Rodoviário**

**(1)** Acesse a tela ''Ordens de Carga'' (Comercial » Rotinas » Ordem de Carga » Ordens de Carga) e crie a ''Ordem de Carga''. Essa **OC** será utilizada posteriormente para vincular o Pedido ou Nota Fiscal no processo de Formação de Carga.

**(2)** Em seguida, acesse a tela [**''Portal de Vendas''**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612654-Portal-de-Vendas) (Comercial » Consulta » Portal de Vendas) e crie o **Pedido de Venda ou a Nota Fiscal**.

**(3)** Durante a criação do Pedido ou da Nota, realize a **Formação de Carga**, vinculando a Ordem de Carga criada anteriormente. Após esse vínculo, o número da OC ficará associado ao pedido e será exibido posteriormente na NF-e.

**(4)** Caso necessário, acesse a tela [**''Formação de Carga''**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612274-Forma%C3%A7%C3%A3o-de-Carga) (Comercial » Rotinas » Ordem de Carga » Formação de Carga), confira o vínculo entre a OC e o Pedido/Nota e clique em **''Confirmar''** para registrá-lo.

**(5)** Retorne á tela ''Ordens de Carga'' (Comercial » Rotinas » Ordem de Carga » Ordens de Carga) e clique no botão **''Criar Viagem''** para iniciar o processo de emissão da MDF-e.

**(6)** O sistema abrirá automaticamente a tela ''Viagens de Transporte (MDF-e)'' (Comercial » Rotinas » Viagens de Transporte (MDF-e)):

- No **Modal Rodoviário**, o sistema preenche automaticamente os campos **"UF de Coleta"** e **"UF de Descarregamento"** com a origem e o destino da viagem. Caso a rota passe por outros estados, a SEFAZ validará o percurso. Nesses casos, é necessário informar as UFs adicionais na sub-aba **"UFs do Percurso"**.
- Para **CT-e**, as abas **Contratantes, Seguro, CIOT, Vale Pedágio** e **Lacres** são obrigatórias.
- Para **NF-e**, essas abas não são necessárias.

**(7)** Após o preenchimento das informações, é possível gerar **XML para conferência**, incluir eventos, gerar contingência e imprimir MDF-e Normal ou Contingência.

**(8)** Com a MDF-e devidamente lançada, gere o lote para enviá-la a SEFAZ e aguarde a autorização.

**(9)** Em casos de rejeição, utilize o botão **''MDF-e''** e clique em **''Ver Acompanhamentos''** para consultar os detalhes.

**(10)** Após a MDF-e ser aprovada, clique em **"Encerrar"** para finalizar o documento e liberar o veículo para futuras viagens.

**2. Modal Aquaviário**

**(1)** Acesse a tela [**''Veículos''**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111533-Ve%C3%ADculos) (Configurações » Cadastros » Veículos) para cadastrar corretamente o veículo aquaviário.

**(2)** Na aba **''Propriedades''** defina o campo **''Tipo de Veículo''** como **''Aquaviário''**.

**(3)** Já na aba **''Embarcação''**, preencha as informações conforme o registro do Ministério dos Portos:

- **Código da Embarcação**
- **Tipo de Embarcação** (11 – Empurrador ou 39 – Balsa, atualmente suportados)
- **Nome da Embarcação**

**(4)** Em seguida, acesse a tela ''Portal de Vendas'' e crie uma **CT-e**.

**(5)** No cabeçalho da CT-e, é obrigatório o preenchimentos dos campos:

- 'Valor AFRMM'
- 'Vlr. Prest. AFRMM'
- 'IRIN do Navio'
- 'Identificação do navio'
- 'Direção da viagem'

Caso aplicável, também podem ser informados os campos:

- ID. da Balsa 1 - 'Se necessário'
- ID. da Balsa 2 - 'Se necessário'
- ID. da Balsa 3 - 'Se necessário'

**(6)** Após a criação do CT-e, e acesse a tela ''Ordens de Carga'' (Comercial » Rotinas » Ordem de Carga » Ordens de Carga) e crie uma **Ordem de Carga** utilizando um veículo **do tipo Aquaviário**.

**(7)** Realize a **Formação de Carga**, vinculando essa Ordem de Carga ao CT-e criado anteriormente. Com o vínculo concluído, acesse a ''Ordens de Carga'' e clique em **''Criar Viagem''**.

**(8)** O sistema abrirá automaticamente a tela ''Viagens de Transporte (MDF-e)'' (Comercial » Rotinas » Viagens de Transporte (MDF-e)), já com o **Modal MDF-e** definido como **Aquaviário**.

Nesse modal:

- As abas **UFs do Percurso**, **Contratantes** e **Seguro** **não são obrigatórias**.
- As informações de **Terminais de Carregamento**, **Terminais de Descarregamento**, **Embarcações do Comboio**, **Unidade de Carga Vazia** e **Unidades de Transporte Vazias** são **opcionais**, variando conforme o processo operacional do cliente.

**(9)** Após o preenchimento das informações necessárias, gere o lote para enviar a MDF-e á SEFAZ e aguarde a autorização.

**(10)** Com a MDF-e aprovada, clique em **''Encerrar''** para registrar o evento de encerramento, concluindo o ciclo da MDF-e e liberando o veículo para novas viagens.

**3. Emissão de MDF-e por terceiros (sem Ordem de Carga)**

Nos casos em que o transporte é realizado por **terceiros**, a emissão da MDF-e **não utiliza o fluxo de Ordem de Carga**. Nessa modalidade, o manifesto é criado diretamente na rotina de viagens, sem a necessidade de vínculo prévio com OC.

**(1)** Acesse a tela ''Viagens de Transporte (MDF-e)'' (Comercial » Rotinas » Viagens de Transporte (MDF-e)) e realize a emissão.

**(2)** Efetue o lançamento do manual da MDF-e, informando os dados obrigatórios, como:

- Documentos fiscais vinculados (NF-e ou CT-e);
- Dados do transportador responsável;
- Veículo e condutor;
- Origem, destino e, quando aplicável, as **UFs do Percurso**.

Após o preenchimento das informações, o processo segue o fluxo padrão de emissão da MDF-e, incluindo:

- Geração do XML para conferência;
- Transmissão do lote para aprovação na SEFAZ;
- Consulta de rejeições, quando houver;
- Encerramento da MDF-e após a aprovação, liberando o veículo para novas viagens.

**PERGUNTAS:**

- **Porque o DAMDFE não imprime a relação das Notas?**

Somente o modelo DAMDFE Contingência imprime a relação das notas que compõem a MDF-e.

**Caso prático**: Em fiscalizações em barreiras, o fisco realiza a leitura (“bipagem”) do código de barras da MDF-e e, no sistema da SEFAZ, são apresentados todos os dados do manifesto, inclusive as NF-e que compõem a CT-e, dispensando a impressão dessa informação no DAMDFE normal. Já quando o documento é emitido em **contingência**, a MDF-e ainda não está aprovada pela SEFAZ. Nesse cenário, torna-se necessária a impressão da relação das notas no DAMDFE para apresentação em fiscalização.

- **É possível incluir mais de um Condutor para a MDF-e?**

Sim. A MDF-e permite o cadastro de no mínimo 1 (um) e no máximo 10 (dez) condutores, por meio de um evento específico.

**Caso prático:** Após a MDF-e estar aprovada e antes de encerramento, acesse o menu ''**MDF-e''** e selecione **''Incluir Condutor''**. Informe o parceiro correspondente ao motorista e confirme a operação.

Na sub-aba **''Eventos''**, será registrado e assinado o evento **110114 - Inclusão Condutor**.

- **Uma NF-e vinculada a uma MDF-e já encerrada, posso vincula-la novamente em uma nova MDF-e?**

Sim, o sistema não impede que a NF-e já vinculada a uma MDF-e encerrada seja utilizada em uma nova MDF-e.

Para evitar problemas de fiscalizações, localize a aba **''Geral''**, sub-aba **''Documentos MDF-e''** e marque o campo **''Id.Reentrega''**.

Essa marcação indica que se trata de uma nova tentativa de entrega, sem gerar implicações legais em barreiras fiscais.

**OBSERVAÇÃO:**
Manual do Contribuinte:
<https://mdfe-portal.sefaz.rs.gov.br/Site/Documentos>
