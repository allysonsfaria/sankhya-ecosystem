---
id: "360044598034"
titulo: "Modelo de Impressão (Nota/Pedido)"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044598034-Modelo-de-Impress%C3%A3o-Nota-Pedido"
trilha: "Manual do Produto > Comercial e Vendas > Comercial > Comercial"
atualizado_em: "2026-08-14T23:18:40Z"
rotulos: ["CT-e", "AJUDA DO SKW", "manual", "Configuração", "Impressão", "Relatórios Formatados", "PARÂMETROS PNOMEUSULOGADO E PCODUSULOGADO", "Nota Fiscal Eletrônica", "Download", "Relatório Dependente", "DANFE", "IReport", "Modelo de Impressão (Nota/Pedido)", "br.com.sankhya.modelo.impressao.nota.pedido", "Modelo de Impressão (Nota/Pedido) manual", "Nota Fiscal", "Modelos de Impressão", "Baixar Modelos Padrões", "Notas/Pedidos", "Comercial"]
---

# Modelo de Impressão (Nota/Pedido)

```
![Imagem 1](https://ajuda.sankhya.com.br/hc/article_attachments/42311751922839) Módulo: Comercial > Arquivo > Cadastros
```

---

Através desta tela, realizamos a criação de modelos para impressão de Notas/Pedidos, DANFE, DACTE's; além disso, podemos baixar um dos modelos padrão do sistema, que poderão ser alterados conforme a necessidade.

**Importante:** Quando na criação de um novo modelo, este deve ser criado primeiramente no iReport, antes de ser adicionado a esta tela.

![Imagem 2: Importante: Quando na criação de um novo modelo, este deve ser criado primeiramente no iReport , antes de ser…](https://ajuda.sankhya.com.br/hc/article_attachments/1500015006861)

Para criação de um novo modelo, clique no botão de inserção (Novo) no painel de controle; identificamos o novo registro através dos campos:

**Código:** Será gerado automaticamente pelo sistema.

**Descrição:** Identificação do registro fornecida por você.

**Última Alteração:** Data e hora de criação do novo registro, que serão preenchidos automaticamente pelo sistema e servirá pra consultas futuras.

**Usuário:** O sistema automaticamente irá registrar o nome e código do usuário logado, que foi o responsável pela criação ou alteração do modelo.

**Relatório Dependente:** Se houver necessidade de vincular outro modelo de Relatório Formatado a este, informe neste campo o código do relatório dependente. É utilizado, por exemplo, para que, no envio de Notas Fiscais por e-mail, seja enviado também o boleto, ou qualquer outro relatório relacionado ao faturamento.

No campo **"Nome do anexo no envio de e-mail"** você pode informar o nome do arquivo da nota fiscal que é encaminhado via e-mail através da tela [Impressão de Boleto(s)](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044607094); isso, quando a marcação **"Anexar Nota Fiscal"** disponível no acionamento do botão **"Enviar boleto(s) por e-mail"** estiver realizada. Por exemplo, informando no campo Nome do anexo no envio de e-mail o nome **"Venda Total"**, a nota anexada no e-mail enviado terá o nome **"Venda Total\_número da nota"**. Caso o campo seja mantido em branco, o arquivo enviado em anexo no e-mail, terá o nome padrão de **"Nota\_fiscal\_número da nota"**.

**Observação:** O envio do XML e do DANFE da NFC-e por e-mail utiliza as **mesmas configurações aplicadas ao envio da NF-e**.

Além dos botões padrões do painel, a tela possui as opções de **"Visualizar"** e **"Agendar Relatório"**.

O botão **"Baixar Modelos Padrões"** contém modelos padrões de **"DANFE Retrato e Paisagem"**, **"Nota/Pedido"**, **"DANFE NFCe Completo e Simplificado"** e **"DACTE Retrato"** para download. Através deste botão, temos as seguintes opções:

- Modelo DANFE Retrato 3.0;
- Modelo DANFE Paisagem 3.0;
- Modelo DANFE Retrato 4.0;
- Modelo DANFE Paisagem 4.0;
- Modelo DANFE Simplificado Etiqueta;
- Modelo Nota/Pedido;
- Carta de Correção;
- Carta de Correção CT-e
- Modelo DANFE NFCe Completo;
- Modelo DANFE NFCe Simplificado;
- Modelo DANFE NFCe Completo TXT;
- Modelo DANFE NFCe Simplificado TXT;
- Modelo DACTE Retrato;
- Modelo DACTE Retrato 3.0 Rodoviário;
- Modelo DACTE Retrato 3.0 Rodoviário (QR Code);
- Modelo DACTE Retrato Multimodal;
- Modelo DACTE-OS Retrato;
- Modelo DACTE-OS Retrato (QR Code);
- Modelo DACTE Retrato 3.0 Aquaviário;
- Modelo DACTE Retrato 3.0 Aquaviário (QR Code);
- Modelo DAMDFe Retrato;
- Modelo DAMDFe Retrato Contingência;
- Modelo DAMDFe Paisagem;
- Modelo DAMDFe Paisagem Contingência;
- Modelo DAMDFe Paisagem Aquaviário;
- Modelo DAMDFe Paisagem Contingência Aquaviário;
- Modelo DAMDFe Retrato Aquaviário;
- Modelo DAMDFe Retrato Contingência Aquaviário;
- Modelo CF-e;
- Modelo CF-e de Cancelamento;
- Modelo Padrão NFS-e Nacional.

![Imagem 3: Modelo Padrão NFS-e Nacional.](https://ajuda.sankhya.com.br/hc/article_attachments/1500015006941)

**Observação:** Em relação ao Modelo Padrão, considerando a opção **"Modelo DACTE-OS Retrato"**, ao gerar a nota e imprimi-la, não serão preenchidos os campos **"TERMO DE AUTORIZAÇÃO DE FRETAMENTO"**, **"N. DE REGISTRO ESTADUAL"** e **"PERCURSO DO VEÍCULO"**, pois estas informações não serão disponibilizadas no xml.

**Nota:** O Modelo de Impressão (Nota/Pedido) está associado à versão do DACTE ou NF-e cadastrado nas [Preferências da Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Empresa). Abaixo temos um exemplo:

Na tela Preferências da Empresa, aba [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa#abageral), temos o campo **"Versão CT-e"** com duas opções disponíveis para escolha, sendo estas, a **"Versão CT-e 3.00"** e **"Versão CT-e 2.00"**. Assim, o Modelo de Impressão para a opção Versão CT-e 3.00 seria o **"Modelo DACTE Retrato 3.0 Rodoviário"** e para a opção Versão CT-e 2.00 o **"Modelo DACTE Retrato"**.

Através da opção **"Carta de Correção CT-e"**, será possível baixar o modelo de impressão de um Conhecimento de Transporte Eletrônico e, posteriormente, adicioná-lo nas Preferências da Empresa, sub-aba [CT-e](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa#Sub-abaCT-e), campo **"Relatório Carta de Correção"**.

**Observação:** Para realizar a impressão desta Carta de Correção CT-e, acesse o [Portal de Vendas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612654-Portal-de-Vendas), acione o botão **"CT-e"** (localizado no alto da tela) e selecione a opção **"Imprimir a Carta de Correção"**.

O download permite que você customize o modelo da forma que melhor lhe atenda. Os downloads trazem cada arquivo em formato **".zip"**.

Ao descompactar esse arquivo, com um programa adequado para isso (WinRar, WinZip, 7Zip, etc), estarão disponíveis os modelos para serem alterados e posteriormente inseridos nesta tela.

![Imagem 4: Ao descompactar esse arquivo, com um programa adequado para isso (WinRar, WinZip, 7Zip, etc), estarão disponíveis os…](https://ajuda.sankhya.com.br/hc/article_attachments/1500015007281)

**Importante:** Em relação ao DANFE é necessário que:

1. Seja feita a baixa do modelo desejado ou a criação de um novo modelo, inserindo-o posteriormente nesta rotina;
2. Realize o cadastro deste modelo na tela de [Relatórios Formatados](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045108573-Relat%C3%B3rios-Formatados-);
3. Nas [Preferências da Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Empresa), aba [NF-e/NFC-e](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Empresa#abanf-enfc-e), campo **"Relatório Formatado DANFE"** indique o código do relatório em que o DANFE foi cadastrado.

Depois de salvar o cabeçalho com as informações sobre o novo registro, adicione o novo arquivo configurado pelo iReport ou baixado pelo botão **"Baixar Modelos Padrões"**. Isto será feito pelo botão **"Adicionar Arquivo..."** presente na aba **"Arquivos"**.

**Nota:** O sistema aceitará apenas arquivos no formato **".jrxml"**.

O Sankhya OM permite que sejam adicionados mais de um arquivo para cada modelo, tudo através do botão **"Adicionar Arquivos"**.

O botão **"Download"** apenas ficará habilitado após a adição de um arquivo. Em caso de perda do modelo original, você poderá resgatar o mesmo através do download, tanto para alteração no arquivo, quanto para conferência dos dados.

#### Geração de grandes relatórios

Ao realizar uma consulta, utilizando-se de poucos filtros, em grandes bancos de dados, pode-se obter como resultado, grandes relatórios. O tamanho destes documentos podem consumir toda a memória principal (RAM) disponível, ou até mesmo fazer com que o Sankhya OM perca sua conexão.

Na geração de um grande relatório através desta tela, é permitido ao sistema utilizar a virtualização do **"JasperReports"** (framework utilizado no Sankhya OM para geração dos relatórios em PDF e Excel(XLSX)), para que o processo de geração seja feito em memória secundária (HD), não consumindo assim, toda a memória principal (RAM) disponível.

**Importante:** Caso seja necessária a configuração para geração de um relatório com grandes quantidades de informação, esta deve ser realizada por um Consultor Sankhya.

#### Parametrização

**Parâmetros PNOMEUSULOGADO e PCODUSULOGADO**

Imprimir Nome e Código do Usuário logado no momento da impressão de cheques

Os parâmetros Nome do Usuário logado - PNOMEUSULOGADO e Código do Usuário logado - PCODUSULOGADO para utilização de impressão de notas/pedidos e boletos, se habilitados, servem para identificar o usuário logado no momento da impressão dos boletos e das notas.

Para configuração é necessário que você:

- Vá ao IReport, crie os dois parâmetros e posicione-os onde deverão ser impressos:

![Imagem 5: Vá ao IReport, crie os dois parâmetros e posicione-os onde deverão ser impressos:](https://ajuda.sankhya.com.br/hc/article_attachments/360060987414)

Nas propriedades do parâmetro é necessário:

- Parâmetro PNOMEUSULOGADO:

![Imagem 6: Parâmetro PNOMEUSULOGADO :](https://ajuda.sankhya.com.br/hc/article_attachments/360060987434)

- Parâmetro PCODUSULOGADO:

![Imagem 7: Parâmetro PCODUSULOGADO :](https://ajuda.sankhya.com.br/hc/article_attachments/360061915173)

Assim, ao efetuar a impressão da nota, trará a seguinte informação:

![Imagem 8: Assim, ao efetuar a impressão da nota, trará a seguinte informação:](https://ajuda.sankhya.com.br/hc/article_attachments/360060987454)
