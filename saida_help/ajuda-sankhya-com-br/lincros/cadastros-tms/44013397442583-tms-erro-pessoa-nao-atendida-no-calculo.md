---
id: "44013397442583"
titulo: "[TMS] - Erro Pessoa Não Atendida no Cálculo do Pré-conhecimento e CT-e: Causa e Solução"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44013397442583--TMS-Erro-Pessoa-N%C3%A3o-Atendida-no-C%C3%A1lculo-do-Pr%C3%A9-conhecimento-e-CT-e-Causa-e-Solu%C3%A7%C3%A3o"
trilha: "Lincros > TMS > Cadastros - TMS"
atualizado_em: "2026-10-05T19:57:09Z"
rotulos: ["sync_hc", "lincros", "lincros_13432531", "sync_hash_b83d8a9019f3"]
---

# [TMS] - Erro Pessoa Não Atendida no Cálculo do Pré-conhecimento e CT-e: Causa e Solução

## Problema Relatado pelo Cliente

O cliente reportou que os Pré-Conhecimentos para um determinado destinatário e cidade não estavam sendo calculados corretamente. Ao tentar recalcular, o sistema exibia a mensagem de erro: "Pessoa não atendida". O cliente solicitou esclarecimentos sobre a causa desse problema.

---

## Passo a Passo para Resolver o Problema

- **Compreensão do Erro:**
  A mensagem "Pessoa não atendida" indica que a tabela de frete que deveria ser utilizada no cálculo possui uma restrição por pessoa.
- **Identificação da Restrição:**
  O provável motivo para o erro é que o CNPJ do destinatário do documento está cadastrado como uma restrição de busca na tabela de frete.
- ## Verificação na Tabela de Frete:

  - Acesse a tabela de frete que deveria ser utilizada no cálculo do pré-conhecimento/ CT-e em Cadastros Gerais> Transportadoras> Negociações> Tabelas de Frete.
  - Localize a aba **"Restrições de Busca"**.
  - Verifique se o CNPJ do destinatário está informado como uma restrição.
- **Correção da Restrição:**
  Caso o CNPJ esteja listado como restrição e isso não seja intencional, remova-o ou ajuste as configurações da tabela para permitir o cálculo correto do frete. Há três tipos de restrições:

- - Atendido (ícone de bolinha verde) - significa que o sistema irá priorizar essa tabela de frete para ser selecionada no cálculo do frete do pré-conhecimento, caso todos os demais requisitos sejam atendidos. Se mais de uma tabela de frete possuir a mesma pessoa com restrição Atendido, o sistema vai buscar uma dessas tabelas de frete e escolher de acordo com o critério determinado no parâmetro de empresa (menos valor ou melhor prazo).
  - Exclusivo (ícone de bolinha amarela) - significa que o sistema irá puxar exclusivamente essa tabela de frete para cálculo do frete do pré-conhecimento. Para o funcionamento correto do processo, não pode existir mais de uma tabela de frete com a mesma pessoa informada como Exclusivo.
  - Restrito (ícone de bolinha cinza) - significa que o sistema não vai considerar essa tabela de frete para cálculo do pré-conhecimento que tiver essa pessoa informada.
- **Testes e Validação:**
  Após a alteração, tente recalcular o CT-e para verificar se o problema foi resolvido.

![Imagem 1: Testes e Validação: Após a alteração, tente recalcular o CT-e para verificar se o problema foi resolvido.](https://ajuda.sankhya.com.br/hc/article_attachments/44013406129687)
