---
id: "43548401689367"
titulo: "Erro: O custo ABC não foi implementado para Reprocesso!"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/43548401689367-Erro-O-custo-ABC-n%C3%A3o-foi-implementado-para-Reprocesso"
trilha: "Solução de Problemas > Produção"
atualizado_em: "2026-09-25T11:33:56Z"
rotulos: ["Artigo criado KCS", "Produção - KCS"]
---

# Erro: O custo ABC não foi implementado para Reprocesso!

**Mensagem**

**O custo ABC não foi implementado para Reprocesso!**

**Situação**

Ao tentar acessar o custo previsto e/ou médio pela tela **Custo Curva ABC** na tela **Composição do Produto** (Produção » Cadastros » Composição do Produto), botão **'Ver Custos'**, envolvendo **Processos Produtivos** do tipo **reprocesso**, o sistema apresenta a mensagem informando que o custo ABC não está disponível para este tipo de análise.

**Solução**

**(1)** Consulte os custos previstos e médios das **MPs** (Matérias-primas) utilizadas na composição do produto, pela tela de **Variação de Custos de Produtos** (Comercial » Consulta » Variação de Custos de Produtos) e valide os custos por esta tela.

**(2)** Acompanhe as atualizações do sistema, pois a implementação da análise de **Custo Curva ABC** para **Processos Produtivos (**Produção » Cadastros » Processo Produtivo - Nova**)** do tipo reprocesso está prevista para futuras versões.

**Causa**

O sistema não contempla o cálculo do Custo Curva ABC para operações de reprocesso, pois a metodologia ABC foi implementada inicialmente apenas para processos produtivos padrão. O reprocesso possui particularidades de consumo e reaproveitamento de materiais que ainda não foram contempladas na lógica do cálculo ABC, estando sua implementação prevista para versões futuras.
