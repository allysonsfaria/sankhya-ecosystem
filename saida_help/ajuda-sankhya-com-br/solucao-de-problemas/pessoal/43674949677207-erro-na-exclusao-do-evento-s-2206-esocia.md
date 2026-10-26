---
id: "43674949677207"
titulo: "Erro na exclusão do evento S-2206 eSocial ([536] Informações do Empregador, trabalhador e/ou período de apuração incompatíveis)"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/43674949677207-Erro-na-exclus%C3%A3o-do-evento-S-2206-eSocial-536-Informa%C3%A7%C3%B5es-do-Empregador-trabalhador-e-ou-per%C3%ADodo-de-apura%C3%A7%C3%A3o-incompat%C3%ADveis"
trilha: "Solução de Problemas > Pessoal+"
atualizado_em: "2026-10-02T17:28:16Z"
rotulos: ["Artigo criado KCS", "Sankhya RH - KCS"]
---

# Erro na exclusão do evento S-2206 eSocial ([536] Informações do Empregador, trabalhador e/ou período de apuração incompatíveis)

MENSAGEM

[536] Informações do empregador, trabalhador e/ou período de apuração incompatíveis.

SITUAÇÃO

O erro ocorre ao tentar excluir um evento S-2206 (Alteração Cadastral/Contratual) no eSocial, geralmente após uma tentativa de ajuste na admissão do colaborador. Após a exclusão do evento de admissão ou alteração de dados, o evento de exclusão do S-2206 desaparece da tela e não pode ser reenviado. Ao tentar enviar novamente o evento S-2206, o sistema retorna a mensagem de erro 536, indicando incompatibilidade entre as informações do empregador, trabalhador e/ou período de apuração.

SOLUÇÃO

Siga o passo a passo para corrigir o erro e permitir a exclusão correta do evento S-2206:

1. **(1)**  Acesse a tela **"Cadastro de Funcionários"** Configurações » Cadastros » Pessoal » Configuração Funcionários e verifique a **"Data de Admissão"** do colaborador envolvido no erro.
2. **(2)**  Caso a **"Data de Admissão"** tenha sido alterada após o envio do evento S-2200 ou S-2206, ajuste a data para o valor original, mantendo a mesma que constava no evento já enviado ao eSocial.
3. **(3)**  Após corrigir a data, gere novamente o evento S-2206 de exclusão pela tela **"Central do eSocial"** Pessoal+ » Rotinas Folha » Central do eSocial  e envie o evento ao eSocial.
4. **(4)**  Aguarde o retorno do processamento do evento. Caso o evento seja aceito, prossiga com o reenvio dos eventos necessários, como S-2200 ou S-2206 com as informações corretas.

1. **Regras importantes:**
2. A data **não pode ser anterior** ao último S-2205 ou S-2206 enviado
3. A data **não pode ser futura** (maior que a data atual)
4. A data deve estar dentro do **período de obrigatoriedade** do eSocial para sua empresa

💡 **Dica**: Se houver eventos de folha (S-1200, S-1210) posteriores à data da alteração, você precisará excluí-los primeiro, pois o eSocial não permite exclusão de eventos com dependências.

Se o erro persistir, revise se há divergências em outros campos do cadastro do colaborador que possam impactar a compatibilidade das informações enviadas.

CAUSA

##

O erro geralmente ocorre quando:

- **Data da alteração** é incompatível com eventos já enviados (anterior ou igual a um S-2205, S-2206 ou S-2200 já transmitido)
- **Matrícula do funcionário** não corresponde ao vínculo ativo no eSocial
- **CPF do trabalhador** está divergente ou incorreto
- **CNPJ do empregador** está inválido ou não corresponde ao cadastro
- Existe **duplicidade de eventos** para a mesma data de alteração
- Há **eventos posteriores** já enviados que se tornariam inconsistentes
- **Período de apuração** está fora da sequência cronológica
