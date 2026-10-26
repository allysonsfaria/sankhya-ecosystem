---
id: "41060869326871"
titulo: "Como funciona a emissão de notas fiscais com CNPJ alfanumérico"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/41060869326871-Como-funciona-a-emiss%C3%A3o-de-notas-fiscais-com-CNPJ-alfanum%C3%A9rico"
trilha: "Manual do Produto > Fiscal e Contábil > Reforma Tributária > Notícias e novidades"
atualizado_em: "2026-07-29T13:14:17Z"
rotulos: ["Configuração", "CNPJ", "NF-e", "Atualização", "SEFAZ", "Documentos Eletrônicos"]
---

# Como funciona a emissão de notas fiscais com CNPJ alfanumérico

Versão mínima ERP Core 5.7.0
Versão mínima Livros 5.36.8
Versão mínima Sankhya OM 4.36b63

---

## O que é e para que serve

A emissão de notas fiscais com CNPJ alfanumérico permite que o Sankhya Om processe, valide e autorize documentos fiscais para empresas registradas sob o novo padrão da Receita Federal (combinação de letras e números nas 12 primeiras posições). Ela serve para garantir a continuidade das operações fiscais com novos parceiros e evitar rejeições de formato nos órgãos autorizadores.

## O que foi adequado no sistema

As rotinas fiscais foram atualizadas de forma transparente para suportar o novo leiaute sem interromper o fluxo atual:

- **Schemas XSD:** validações de estrutura atualizadas para os modelos 55, 65, 57, 67, 58 e 62.
- **Chave de Acesso:** a composição das 44 posições agora suporta caracteres alfanuméricos na porção correspondente ao CNPJ (modelos 55, 65, 57, 67, 58 e 62).
- **Códigos de barras:** a impressão do DANFE, DACTE e DAMDFE alterna dinamicamente a simbologia entre CODE-128C (para CNPJs numéricos) e CODE-128A (para CNPJs alfanuméricos).
- **EFD-Reinf:** eventos adaptados para comportar o formato nas informações de retenção e obrigações acessórias.

| **Atenção**  Os testes de emissão de NF-e e NFC-e só estarão disponíveis a partir de 15 de junho de 2026. |
| --- |

## Como funciona a validação

Ao emitir uma nota para um parceiro com o novo formato, o sistema valida a estrutura do CNPJ automaticamente antes do envio à SEFAZ. Se desejar, você pode confirmar a situação cadastral do parceiro acessando diretamente o [Portal da Receita Federal.](https://servicos.receitafederal.gov.br/servico/cnpj-alfa/validar)

| **Nota**  Empresas abertas até julho de 2026 mantêm seu CNPJ 100% numérico sem alterações. Somente novos registros a partir dessa data receberão o formato alfanumérico. O Sankhya Om aceita e processa ambos os formatos simultaneamente. |
| --- |

| **Dica**  Para homologar as emissões no ambiente de testes da SVRS (CTe, MDFe, entre outros), utilize o CNPJ de teste disponibilizado pela [SEFAZ](https://dfe-portal.svrs.rs.gov.br/DFE/Avisos/2978): preencha o documento com **PC3D315K000193** e a Inscrição Estadual com **0018001360** (SEFAZ RS). |
| --- |
