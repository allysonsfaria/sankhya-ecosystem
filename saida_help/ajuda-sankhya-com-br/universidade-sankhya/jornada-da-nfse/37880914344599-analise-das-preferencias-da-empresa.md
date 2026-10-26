---
id: "37880914344599"
titulo: "Analise das preferências da Empresa"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37880914344599-Analise-das-prefer%C3%AAncias-da-Empresa"
trilha: "Universidade Sankhya > Jornada da NFSe"
atualizado_em: "2026-07-22T14:06:16Z"
rotulos: ["Configuração", "Empresa", "Fiscal", "Impostos", "Prefeituras", "NFS-e"]
---

# Analise das preferências da Empresa

## Preferências da Empresa

As Preferências da Empresa concentram os parâmetros que habilitam a emissão de NFS-e por CNPJ: município competente e regras do ISS, regime tributário/CNAE, certificado digital (e-CNPJ/e-CPF), ambiente (homologação/produção), numeração/série de RPS e credenciais exigidas pela prefeitura. Essas definições abastecem o XML/RPS e se conectam a cadastros de Serviço e à TOP para aplicar alíquota, retenção e deduções conforme o layout municipal. Também reúnem opções de PIS/COFINS/CSLL e créditos, garantindo consistência entre nota, livros e financeiro. Um cadastro coerente aqui evita rejeições, divergências de cálculo e assegura a transmissão e escrituração corretas.

#### Siga as orientações para realizar a configuração no ERP Sankhya

1. Acesse a tela **Empresa**
   **Menu:** Comercial » Preferências » Empresa

- Localize e selecione o registro da empresa
- Valide os dados registrados:

**Aba Propriedade**

- Ativo - **marcado**
- Calcula IRRF ? -  **marcado**
- Calcula FUNRURAL/INSS? - **marcado**
- ISS -  **”Tributado”**

**Aba Documentos Fiscais Eletrônicos**
**Sub aba NFSe**

- Agrupar serviços faturamento? - **marcado**
- Marcar nota como RPS por padrão -- **marcado**
  Quando marcado, o parâmetro envia automaticamente o lote de NFS-e, dispensando a etapa “Buscar Autorização”. Quando desmarcado, após confirmar a NFS-e na Central de Vendas, é necessário acionar “Buscar Autorização” no Portal de Vendas para obter o retorno (aprovação ou rejeição) da prefeitura.
- Senha NFS-e - **MTIzNDU2**
- Usuário NFS-e - **SUP**
  Nos campos "**Usuário NFS-e**" e "**Senha NFS-e**" é possível configurar o mesmo usuário e a mesma senha que acessa o site da prefeitura para emissão de NFS-e.
- Ambiente NFS-e -**“Homologação”**
  O uso é determinado atráves das seguintes opções:

  - **Homologação**: deverá ser marcada se a empresa estiver em fase de teste, emitindo NFS-e sem validade fiscal.
  - **Produção**: se a empresa já estiver emitindo NFS-e oficialmente com validade fiscal, esta opção deverá ser marcada.
  - **Não usa**: se marcada, indicará que a empresa não emite NFS-e.
- Conteúdo a ser enviado na descrição de NFS-e - **“Descrição + obs. dos itens de serviços + obs. da nota”**
- Regime esp. tributação ISS (NFS-e) - **“T - Tributável**
  [Consulte opções padrão ABRASF](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603434-Nota-Fiscal-Eletr%C3%B4nica-de-Servi%C3%A7o-Prefeituras)
- Tipo de Transmissão NFS-e -**“Automática”**
- **Aba CNAE Empresa**
- CNAE - **461760000**
- Local tributação (ISS Retido) - **“Cidade do Prestador”**
- Local tributação (ISS normal) - **“Cidade do Prestador”**

Se o parâmetro CIDISSCNAEEMP estiver ligado, o sistema valida o CNAE e o Local de Tributação pela aba “CNAE da Empresa” (Preferências da Empresa). Se estiver desligado, o Local de Tributação considerado será a cidade do prestador do serviço. 

**Atenção!** Para mais orientações sobre o preenchimento correto dos campos, acesse o conteúdo disponível no portal [Ajuda Sankhya](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa).
