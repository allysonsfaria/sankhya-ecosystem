---
id: "33530519591063"
titulo: "Geração de Dados de Unidades de Transporte e Carga no MDF-e (funcionalidade, tela) - Rodoviário NF-e"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/33530519591063-Gera%C3%A7%C3%A3o-de-Dados-de-Unidades-de-Transporte-e-Carga-no-MDF-e-funcionalidade-tela-Rodovi%C3%A1rio-NF-e"
trilha: "Manual do Produto > Fiscal e Contábil > Fiscal > Documentos Fiscais Eletrônicos > MDF-e"
atualizado_em: "2026-09-15T16:53:23Z"
rotulos: ["MDF-e", "CT-e", "XML", "SEFAZ", "Rodoviário", "Transporte", "Ordens de Carga", "nf-e", "Ordem de Carga  Rodoviário  Viagens de Transportes (MDF-e)  Geração de Dados de Unidades de Transporte e Carga no MDF-e (funcionalidade tela) - CT-e  Notas do Conhecimento de Transporte;", "Geração de Dados de Unidades de Transporte e Carga no MDF-e (funcionalidade tela) - Rodoviário NF-e", "Documentos Eletrônicos"]
---

# Geração de Dados de Unidades de Transporte e Carga no MDF-e (funcionalidade, tela) - Rodoviário NF-e

**Módulo:** Comercial / Fiscal

**Versão Mínima:** A partir da 4.17.0

**Telas relacionadas:**

- Comercial > Rotinas > Central de Vendas > Notas do Conhecimento de Transporte
- Comercial > Rotinas > Ordem de Carga
- Comercial > Rotinas > Viagens de Transportes (MDF-e)

---

## Sumário

- [Descrição e Usabilidade](https://ajuda.sankhya.com.br/hc/pt-br/articles/33530519591063-Gera%C3%A7%C3%A3o-de-Dados-de-Unidades-de-Transporte-e-Carga-no-MDF-e-funcionalidade-tela-Rodovi%C3%A1rio-NF-e#h_01K0C51A9PY5M51YV9J3QJKA9K)
  - [Descrição da Funcionalidade](https://ajuda.sankhya.com.br/hc/pt-br/articles/33530519591063-Gera%C3%A7%C3%A3o-de-Dados-de-Unidades-de-Transporte-e-Carga-no-MDF-e-funcionalidade-tela-Rodovi%C3%A1rio-NF-e#h_01K0C51A9PSR2QVXKTDDST88RR)
  - [Pré-requisitos](https://ajuda.sankhya.com.br/hc/pt-br/articles/33530519591063-Gera%C3%A7%C3%A3o-de-Dados-de-Unidades-de-Transporte-e-Carga-no-MDF-e-funcionalidade-tela-Rodovi%C3%A1rio-NF-e#h_01K0C51A9QRBQAQF8D9R4PFKBR)
  - [Diagrama de Fluxo](https://ajuda.sankhya.com.br/hc/pt-br/articles/33530519591063-Gera%C3%A7%C3%A3o-de-Dados-de-Unidades-de-Transporte-e-Carga-no-MDF-e-funcionalidade-tela-Rodovi%C3%A1rio-NF-e#h_01K0C51A9W3FPJ01RNBAP0EEXT)
  - [Jornada de Uso](https://ajuda.sankhya.com.br/hc/pt-br/articles/33530519591063-Gera%C3%A7%C3%A3o-de-Dados-de-Unidades-de-Transporte-e-Carga-no-MDF-e-funcionalidade-tela-Rodovi%C3%A1rio-NF-e#h_01K0C51A9XMT16F36DQT816JY7)
  - [Pontos de Atenção](https://ajuda.sankhya.com.br/hc/pt-br/articles/33530519591063-Gera%C3%A7%C3%A3o-de-Dados-de-Unidades-de-Transporte-e-Carga-no-MDF-e-funcionalidade-tela-Rodovi%C3%A1rio-NF-e#h_01K0C51AA4QMBMD24HNRA6BZ2Q)
  - [Dicas de Usabilidade](https://ajuda.sankhya.com.br/hc/pt-br/articles/33530519591063-Gera%C3%A7%C3%A3o-de-Dados-de-Unidades-de-Transporte-e-Carga-no-MDF-e-funcionalidade-tela-Rodovi%C3%A1rio-NF-e#h_01K0C51AA87YF0656QSD4B5YE1)
  - [Casos de Uso](https://ajuda.sankhya.com.br/hc/pt-br/articles/33530519591063-Gera%C3%A7%C3%A3o-de-Dados-de-Unidades-de-Transporte-e-Carga-no-MDF-e-funcionalidade-tela-Rodovi%C3%A1rio-NF-e#h_01K0C51AABPBGPQ1AC5FWHM1QN)
- [FAQ – Dúvidas Frequentes](https://ajuda.sankhya.com.br/hc/pt-br/articles/33530519591063-Gera%C3%A7%C3%A3o-de-Dados-de-Unidades-de-Transporte-e-Carga-no-MDF-e-funcionalidade-tela-Rodovi%C3%A1rio-NF-e#h_01K0C51AADX77HD9N65S7TZRXV)
- [Artigos Relacionados](https://ajuda.sankhya.com.br/hc/pt-br/articles/33530519591063-Gera%C3%A7%C3%A3o-de-Dados-de-Unidades-de-Transporte-e-Carga-no-MDF-e-funcionalidade-tela-Rodovi%C3%A1rio-NF-e#h_01K0C51AAGHCNYP9ZG78ENMTYD)

## Descrição e usabilidade

---

### Descrição da funcionalidade

---

Esta funcionalidade garante que as informações de Unidades de Transporte (infUnidTransp) e Unidades de Carga (infUnidCarga), quando preenchidas no CT-e (Conhecimento de Transporte Eletrônico, modelo 57) ou na Ordem de Carga, sejam corretamente geradas no XML do MDF-e e apresentadas na impressão do DAMDFE (Documento Auxiliar do MDF-e), especialmente nos casos de emissão em contingência. O sistema assegura conformidade com os manuais oficiais da SEFAZ, evitando rejeições ou inconsistências fiscais e tornando o processo mais seguro e automatizado para o usuário.

---

### Pré-requisitos

- Permissões necessárias: Acesso para emitir CT-e, Ordem de Carga e MDF-e.
- Parâmetros essenciais: Configuração do ambiente de emissão de MDF-e e CT-e (modelo 57).
- Configurações relacionadas:
  - Tipos de unidade de transporte e carga cadastrados corretamente.
  - Permissão para vincular CT-e à Ordem de Carga.
  - Tela de Formação de Carga habilitada no menu.

---

### Diagrama de fluxo

![Imagem 1: Diagrama de fluxo](https://ajuda.sankhya.com.br/hc/article_attachments/33530519590167)

---

### Jornada de uso

Para geração de dados de unidades de transportes e carga no MDF-e, siga os passos abaixo:

1. Emitir um CT-e (Modelo 57) preenchendo todos os dados necessários de transporte e carga.
2. Criar uma Ordem de Carga e, na tela de Formação de Carga, vincular o CT-e.
3. Preencher a aba "Unidades de Transporte" na Ordem de Carga com as informações pertinentes.
4. Clicar em "Criar Viagem".
5. Na tela de Viagens de Transporte (MDF-e), selecionar a viagem criada e clicar em "Confirmar".
6. Transmitir o MDF-e e corrigir eventuais rejeições até obter autorização.
7. Verificar no XML do MDF-e se os grupos infUnidTransp e infUnidCarga estão presentes.
8. Caso a emissão seja em contingência, imprimir o DAMDFE e conferir a exibição dos dados de documentos vinculados, unidade de transporte e unidade de carga.

---

### Pontos de atenção

- As tags infUnidTransp e infUnidCarga só são geradas se houver preenchimento válido no CT-e ou Ordem de Carga.
- Se não houver dados preenchidos, as informações NÃO aparecerão no XML do MDF-e nem no DAMDFE.
- Emissão em contingência exige conferência especial na impressão do DAMDFE para garantir que todas as informações estejam corretas.
- O layout do XML deve ser mantido atualizado conforme o Manual de Orientação do Contribuinte (MOC\_MDFe).
- Alterações nesta rotina podem impactar integrações fiscais e outros módulos do sistema.

---

### Dicas de usabilidade

- Mantenha os cadastros de tipos de unidades de transporte e carga sempre atualizados conforme a legislação vigente.
- Utilize filtros por viagem, data ou CT-e para localizar rapidamente as Ordens de Carga.
- Valide a impressão do DAMDFE em contingência antes de enviá-lo ao cliente ou órgão fiscalizador.
- Preencha todos os campos obrigatórios para evitar rejeições e retrabalho.

---

### Casos de uso

**✅ Exemplo Real:** transportadora emite CT-e rodoviário, preenche a Ordem de Carga com as unidades de transporte, gera o MDF-e e verifica a correta geração das informações tanto no XML quanto no DAMDFE em contingência.

**❌ Erro Comum:** usuário esquece de preencher dados de unidade de carga na Ordem de Carga; ao gerar o MDF-e, as tags não são incluídas no XML, ocasionando inconsistência fiscal.

---

## FAQ – dúvidas frequentes

1. **Preciso preencher as informações de unidade de transporte/carga no CT-e ou Ordem de Carga?**
   Sim, apenas com o preenchimento correto os dados serão levados ao MDF-e.
2. **O que acontece se não preencher as informações?**
   As tags não serão geradas no XML nem exibidas no DAMDFE.
3. **Como valido se as informações foram geradas corretamente?**
   Consulte o XML do MDF-e e a impressão do DAMDFE; as informações estarão visíveis nas seções correspondentes.
4. **Esta rotina atende todos os modais de MDF-e?**
   Não, refere-se especificamente ao modal rodoviário.

---

## Artigos relacionados

- [**Central de Vendas**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas)
- [**Ordens de Carga**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045119713-Ordens-de-Carga)
- [**Viagens de Transportes (MDF-e)**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612514-Viagens-de-Transportes-MDF-e)
