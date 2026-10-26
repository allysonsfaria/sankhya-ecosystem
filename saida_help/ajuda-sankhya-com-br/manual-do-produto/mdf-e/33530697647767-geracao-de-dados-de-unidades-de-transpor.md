---
id: "33530697647767"
titulo: "Geração de Dados de Unidades de Transporte e Carga no MDF-e (funcionalidade, tela) - Aquaviário CT-e"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/33530697647767-Gera%C3%A7%C3%A3o-de-Dados-de-Unidades-de-Transporte-e-Carga-no-MDF-e-funcionalidade-tela-Aquavi%C3%A1rio-CT-e"
trilha: "Manual do Produto > Fiscal e Contábil > Fiscal > Documentos Fiscais Eletrônicos > MDF-e"
atualizado_em: "2026-09-15T16:52:13Z"
rotulos: ["MDF-e", "CT-e", "XML", "SEFAZ", "Aquaviário", "Documentos Eletrônicos"]
---

# Geração de Dados de Unidades de Transporte e Carga no MDF-e (funcionalidade, tela) - Aquaviário CT-e

**Módulo:** Comercial **/** Fiscal

**Versão Mínima:** A partir da 4.17.0

**Telas relacionadas:**

- Comercial > Rotinas > Central de Vendas > Notas do Conhecimento de Transporte;
- Comercial > Rotinas > Ordem de Carga;
- Comercial > Rotinas  > Viagens de Transportes (MDF-e).

---

## Sumário

- [Descrição e Usabilidade](https://github.com/copilot/c/eb018a47-26a7-4565-811f-bf9181c2b700#descri%C3%A7%C3%A3o-e-usabilidade)
  - [Descrição da Funcionalidade](https://github.com/copilot/c/eb018a47-26a7-4565-811f-bf9181c2b700#1-descri%C3%A7%C3%A3o-da-funcionalidade)
  - [Pré-requisitos](https://github.com/copilot/c/eb018a47-26a7-4565-811f-bf9181c2b700#2-pr%C3%A9-requisitos)
  - [Diagrama de Fluxo](https://github.com/copilot/c/eb018a47-26a7-4565-811f-bf9181c2b700#3-diagrama-de-fluxo)
  - [Jornada de Uso](https://github.com/copilot/c/eb018a47-26a7-4565-811f-bf9181c2b700#4-jornada-de-uso)
  - [Pontos de Atenção](https://github.com/copilot/c/eb018a47-26a7-4565-811f-bf9181c2b700#5-pontos-de-aten%C3%A7%C3%A3o)
  - [Dicas de Usabilidade](https://github.com/copilot/c/eb018a47-26a7-4565-811f-bf9181c2b700#6-dicas-de-usabilidade)
  - [Casos de Uso](https://github.com/copilot/c/eb018a47-26a7-4565-811f-bf9181c2b700#7-casos-de-uso)
- [FAQ – Dúvidas Frequentes](https://github.com/copilot/c/eb018a47-26a7-4565-811f-bf9181c2b700#faq--d%C3%BAvidas-frequentes)
- [Artigos Relacionados](https://github.com/copilot/c/eb018a47-26a7-4565-811f-bf9181c2b700#artigos-relacionados)

---

## Descrição e Usabilidade

---

### Descrição da Funcionalidade

Esta funcionalidade garante que, ao emitir o MDF-e no modal Aquaviário, as informações de Unidades de Transporte (infUnidTransp) e Unidades de Carga (infUnidCarga) preenchidas nos documentos de origem (CT-e modelo 57 ou Ordem de Carga vinculada à NF-e) sejam corretamente geradas no XML do MDF-e e exibidas na impressão do DAMDFE – tanto em emissão normal quanto em contingência, conforme os manuais técnicos da SEFAZ/AM. Isso assegura a conformidade fiscal, evitando rejeições e tornando o processo mais seguro e transparente para o usuário.

---

### Pré-requisitos

- Permissões necessárias: Acesso para emitir CT-e, Ordem de Carga e MDF-e modal Aquaviário.
- Parâmetros essenciais: Configuração do ambiente de emissão de MDF-e e CT-e (modelo 57).
- Configurações relacionadas:
  - Tipos de unidade de transporte e carga cadastrados conforme legislação vigente.
  - Permissão para vincular CT-e ou Ordem de Carga à NF-e.
  - Tela de Formação de Carga habilitada.

---

### Diagrama de fluxo

![Imagem 1: Diagrama de fluxo](https://ajuda.sankhya.com.br/hc/article_attachments/33530697646743)

---

### Jornada de Uso

Para geração de dados de unidades de transportes e carga no MDF-e, siga os passos abaixo:

1. Emitir um CT-e (Modelo 57) e/ou emitir uma Ordem de Carga vinculada à NF-e, preenchendo as informações de unidade de transporte e carga.
2. Na tela de Formação de Carga, vincular o CT-e ou Ordem de Carga à NF-e.
3. Certifique-se de que os dados de Unidades de Transporte e Carga estão corretamente preenchidos nas fontes.
4. Criar uma Viagem para o modal Aquaviário.
5. Na tela de Viagens de Transporte (MDF-e), selecionar a viagem e clicar em "Confirmar".
6. Emitir o MDF-e (modal Aquaviário) e transmitir.
7. Validar o XML do MDF-e para verificar a presença dos grupos infUnidTransp e infUnidCarga.
8. Caso a emissão seja em contingência, imprimir o DAMDFE e conferir se as informações obrigatórias de composição da carga aparecem corretamente.

---

### Pontos de Atenção

- As tags infUnidTransp e infUnidCarga só serão geradas se os dados estiverem devidamente preenchidos no CT-e ou Ordem de Carga vinculada à NF-e.
- Para outras modalidades de MDF-e (Rodoviário, Aéreo, Ferroviário, etc.), esta rotina não se aplica.
- Na emissão em contingência, verifique se o DAMDFE está apresentando todos os dados exigidos na seção "Informações da Composição da Carga".
- O leiaute do XML e do DAMDFE deve estar atualizado conforme o Manual de Orientação do Contribuinte e o Manual Técnico da SEFAZ/AM.
- Alterações nesta rotina podem impactar integrações fiscais e outros módulos do sistema.

---

### Dicas de Usabilidade

- Mantenha os cadastros de tipos de unidades de transporte e carga atualizados conforme as exigências legais do modal Aquaviário.
- Utilize filtros por viagem, data ou documento para localizar rapidamente as Ordens de Carga e NFe relacionadas.
- Antes de transmitir, confira se todos os campos obrigatórios estão preenchidos para evitar rejeições e retrabalho.
- Valide a impressão do DAMDFE em contingência antes de encaminhar ao destinatário ou órgão fiscalizador.

---

### Casos de Uso

**Exemplo Real:** empresa de navegação preenche corretamente as unidades de transporte e carga no CT-e e Ordem de Carga vinculada à NF-e, gera o MDF-e Aquaviário e verifica a correta geração das informações tanto no XML quanto no DAMDFE em contingência.

**Erro Comum:** usuário esquece de preencher os dados de unidade de carga; ao gerar o MDF-e Aquaviário, as tags não são incluídas no XML, ocasionando inconsistência fiscal e possível rejeição na SEFAZ/AM.

---

## FAQ – Dúvidas Frequentes

1. **Preciso preencher as informações de unidade de transporte/carga no CT-e ou Ordem de Carga?**
   Sim, apenas se os dados estiverem preenchidos nas fontes, as informações serão levadas ao MDF-e Aquaviário.
2. **O que acontece se não preencher as informações?**
   As tags não serão geradas no XML do MDF-e nem exibidas no DAMDFE, podendo ocasionar rejeição fiscal.
3. **Como valido se as informações foram geradas corretamente?**
   Consulte o XML do MDF-e e a impressão do DAMDFE. As informações estarão visíveis nas seções correspondentes se o preenchimento for correto.
4. **Esta rotina atende todos os modais de MDF-e?**
   Não, aplica-se exclusivamente ao modal Aquaviário.

---

## Artigos Relacionados

- [**Central de Vendas**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas)
- [**Ordens de Carga**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045119713-Ordens-de-Carga)
- [**Viagens de Transportes (MDF-e)**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612514-Viagens-de-Transportes-MDF-e)
