---
id: "44010502439191"
titulo: "[TMS] - Série/CST não definida para o transportador na emissão de CT-e, NFS-e ou MDF-e"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44010502439191--TMS-S%C3%A9rie-CST-n%C3%A3o-definida-para-o-transportador-na-emiss%C3%A3o-de-CT-e-NFS-e-ou-MDF-e"
trilha: "Lincros > TMS > Operacional - TMS"
atualizado_em: "2026-10-05T18:39:36Z"
rotulos: ["sync_hc", "lincros", "sync_hash_cf8319b6b522", "lincros_16911256"]
---

# [TMS] - Série/CST não definida para o transportador na emissão de CT-e, NFS-e ou MDF-e

CT-e NFS-e MDF-e

**Categoria:** Emissão de documentos – Transporte **Módulos:** CT-e · NFS-e · MDF-e **Autoria:** Suporte **Última atualização:** 10/09/2026

## Descrição do erro

Este erro acontece na emissão de CT-e, NFS-e ou MDF-e quando a unidade do transportador não está cadastrada na tela :

**Emissão de documentos – Transporte > Configurações padrões**.

A mensagem exibida varia conforme o documento (por exemplo, "Série e CST não definida para a carga" no pré-conhecimento de CT-e), mas a causa e a correção são as mesmas para os três tipos de documento.

Nesta tela ficam registrados o código do cadastro, a unidade da transportadora, qual transportador é, o CNPJ correspondente e quais tipos de documento — CT-e, NFS-e, MDF-e e CIOT — cada transportadora emite para essa unidade.

![Imagem 1: Nesta tela ficam registrados o código do cadastro, a unidade da transportadora, qual transportador é, o CNPJ…](https://ajuda.sankhya.com.br/hc/article_attachments/44010531648791)

**CAUSA**

A combinação Unidade empresa × Transportadora × Filial transportadora usada na emissão não possui um registro em Configurações padrões para o documento em questão (CT-e, NFS-e ou MDF-e) por isso o sistema não encontra a Série, a Natureza de operação (CST) ou os demais dados padrão a aplicar.

## Padrões de emissão

Essa tela conecta tudo: por Unidade empresa × Transportadora × Filial, e para cada tipo de documento (CT-e, NFS-e, MDF-e ou CIOT), define-se a Série, a Natureza de operação (PJ e PF), a Observação padrão e o modelo de impressão do documento auxiliar (Retrato/Paisagem).

**1 Localize a Unidade empresa, a Transportadora e a Filial transportadora**

Use os campos de busca no topo da tela para localizar o registro correto.

**2 Selecione a aba do documento e habilite a regra**

Escolha a aba correspondente ao documento que apresenta o erro — CT-e, NFS-e ou MDF-e — e clique em **Habilitar regra**. O processo e o preenchimento seguem a mesma lógica em todas as abas, respeitando os campos específicos de cada documento. Na aba CT-e, por exemplo, os campos são:

- Série
- Natureza de operação – Pessoa Jurídica (PJ)
- Natureza de operação – Pessoa Física (PF)
- Observação padrão (quando obrigatória)
- Modelo de impressão do documento auxiliar (Dacte, no caso do CT-e)

**Padrões de emissão: regra habilitada (exemplo na aba CT-e)**

**3 Defina exceções por rota, se necessário**

Se uma rota específica (Estado de origem × Estado de destino) precisa de um padrão diferente do geral, use **Detalhar → Adicionar** para registrar Estado de origem, Estado de destino, Natureza de operação (PJ/PF), Observação padrão e Modelo de impressão dessa exceção, sem alterar o padrão principal.

**✓ COMO RESOLVER**

**Se o erro de Série/CST (ou padrão equivalente) aparecer na emissão de CT-e, NFS-e ou MDF-e, acesse Configurações padrões, selecione a aba do documento correspondente e:**

**1.** Cadastre as informações da unidade desse transportador para o documento em questão, seguindo os passos acima.

**2.** Ou edite o cadastro existente, corrigindo a informação que estiver errada ou incompleta e barrando a emissão.
