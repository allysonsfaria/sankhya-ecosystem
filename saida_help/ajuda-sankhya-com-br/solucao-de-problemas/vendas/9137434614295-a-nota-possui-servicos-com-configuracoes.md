---
id: "9137434614295"
titulo: "A nota possui serviços com configurações diferentes. Seguintes dados devem ser iguais para todos os serviços da nota: Tipo de serviço (Lei cp 116),alíquota de ISS,CNAE e código de tributação do município."
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/9137434614295-A-nota-possui-servi%C3%A7os-com-configura%C3%A7%C3%B5es-diferentes-Seguintes-dados-devem-ser-iguais-para-todos-os-servi%C3%A7os-da-nota-Tipo-de-servi%C3%A7o-Lei-cp-116-al%C3%ADquota-de-ISS-CNAE-e-c%C3%B3digo-de-tributa%C3%A7%C3%A3o-do-munic%C3%ADpio"
trilha: "Solução de Problemas > Vendas"
atualizado_em: "2026-08-06T19:57:43Z"
rotulos: ["Produtos", "Configuração", "Fiscal", "Alíquota de ISS", "Impostos", "CORE_E00580", "CORE_E03912", "NFS-e", "CORE_E06795", "Configurações divergentes", "Verificar e ajustar", "Dados diferentes", "Artigo atualizado KCS", "Docs Eletrônicos - KCS"]
---

# A nota possui serviços com configurações diferentes. Seguintes dados devem ser iguais para todos os serviços da nota: Tipo de serviço (Lei cp 116),alíquota de ISS,CNAE e código de tributação do município.

**Mensagem**

[CORE\_E00580], [CORE\_E03912], [CORE\_E06795]: A nota possui serviços com configurações diferentes. Os seguintes dados devem ser iguais para todos os serviços da nota: **"Tipo de serviço (Lei cp 116)"**, **"Alíquota de ISS"**, **"CNAE"** e **"Código de tributação do município"**.

**Situação**

Este erro ocorre ao tentar emitir uma **"NFS-e"**, gerar lote de **"NFS-e"** ou faturar um contrato, quando o sistema identifica que os serviços possuem configurações divergentes, impedindo a emissão do documento fiscal.

**Solução**

Para resolver este erro, siga os passos abaixo:

**(1)**  Acesse a tela **"Serviço"** (Configurações >> Cadastros >> Produtos) **-> Alíquotas de ISS -> Geral** e valide os campos:

- **Percentual de ISS (Alíquota de ISS)**
- **Cod. Trib. Município (Código de Tributação do Município)**
- **Tipo de Serviço (Lei CP 116)**

  ![Imagem 1: Tipo de Serviço (Lei CP 116)](https://ajuda.sankhya.com.br/hc/article_attachments/41384553725463)

**(2)**  Acesse a aba **"Impostos"** de cada serviço e verifique se os seguintes campos estão idênticos em todos os itens:

- **"Tipo de Serviço (Lei cp 116)"**
- **"CNAE"**
- **"Código de Tributação do Município"**
- **"Código NBS"**

![Imagem 2: Verifique se algum dos serviços possui "Código NCM" preenchido. Caso positivo, remova-o, pois serviços devem conter…](https://ajuda.sankhya.com.br/hc/article_attachments/41384569555735)

**(3)** Verifique se algum dos serviços possui **"Código NCM"** preenchido. Caso positivo, remova-o, pois serviços devem conter apenas o **"Código NBS"**.

**(4)** Padronize as configurações de todos os serviços que serão incluídos na mesma nota fiscal, garantindo que os campos mencionados estejam com os mesmos valores. Após os ajustes, redigite os itens na nota, salve e tente emitir novamente.

**Causa**

O erro ocorre porque o sistema valida que todos os serviços incluídos em uma mesma **"NFS-e"** devem possuir configurações fiscais idênticas. Quando há divergências nos campos de **"Tipo de Serviço"**, **"Alíquota de ISS"**, **"CNAE"**, **"Código de Tributação do Município"** ou **"Código NBS"**, o sistema impede a emissão para evitar inconsistências fiscais.

Além disso, a presença de **"Código NCM"** no cadastro de serviços também pode interferir no cálculo de impostos, gerando divergências que impedem a emissão da nota fiscal.
