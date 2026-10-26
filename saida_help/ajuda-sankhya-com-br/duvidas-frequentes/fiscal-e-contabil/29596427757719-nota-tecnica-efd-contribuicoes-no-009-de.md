---
id: "29596427757719"
titulo: "Nota Técnica EFD-Contribuições nº 009, de 29 de outubro de 2024"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/29596427757719-Nota-T%C3%A9cnica-EFD-Contribui%C3%A7%C3%B5es-n%C2%BA-009-de-29-de-outubro-de-2024"
trilha: "Dúvidas Frequentes > Fiscal e Contábil"
atualizado_em: "2026-07-22T14:37:00Z"
rotulos: ["Configuração", "Impostos", "Nota Técnica", "EFD Contribuições", "NFCom", "Documentos Eletrônicos"]
---

# Nota Técnica EFD-Contribuições nº 009, de 29 de outubro de 2024

Para garantir conformidade com as mudanças estabelecidas na **Nota Técnica nº 009/2024**, o ERP foi atualizado para adequar o leiaute da EFD-Contribuições. Essas mudanças incluem ajustes nos registros **D500 e D600**, além da descontinuação do **Registro 0145 e Bloco P**.

A seguir, detalhamos as principais alterações:

**![Imagem 1: Alterações no Registro D500](https://ajuda.sankhya.com.br/hc/article_attachments/29598330207895) Alterações no Registro D500**

O **Registro D500** foi modificado para incluir um novo tipo de documento fiscal:

- Agora contempla a **Nota Fiscal Fatura de Serviços de Comunicação Eletrônica (NFCom - Código 62)**, conforme exigido pela nova legislação.
- O campo **Chave do Documento Fiscal Eletrônico** (CHV\_DOC\_E) passa a ser obrigatório para documentos dos modelos **55 (NF-e) e 62 (NFCom)**, garantindo maior controle e validação das informações.

**![Imagem 2: Alterações no Registro D600](https://ajuda.sankhya.com.br/hc/article_attachments/29598330211607) Alterações no Registro D600**

O **Registro D600** foi ajustado para consolidar corretamente os documentos fiscais relacionados à prestação de serviços, incluindo:

- Inclusão do modelo **NFCom (Código 62)**, permitindo a escrituração adequada das operações vinculadas a esse documento.
- Atualização dos campos de complementação da prestação de serviços, garantindo a correta apuração dos tributos.

**![Imagem 3: Registro 0145 e Bloco P – Descontinuação](https://ajuda.sankhya.com.br/hc/article_attachments/29598330214551) Registro 0145 e Bloco P – Descontinuação**

Com a descontinuação da obrigatoriedade desses registros a partir de **01/01/2025**, sua geração pode ser desativada diretamente no ERP. Para isso, acesse  **Blocos e Registros** (Comercial > Preferências > Empresa > Aba EFD Escrituração Fiscal Digital > Blocos e Registros).

Caso tenha dúvidas, consulte a documentação oficial da EFD-Contribuições ou entre em contato com o suporte.

**Versões que contemplam as alterações:**

4.33 (monólito)

5.7.XXX (módulo Livros Fiscais)
