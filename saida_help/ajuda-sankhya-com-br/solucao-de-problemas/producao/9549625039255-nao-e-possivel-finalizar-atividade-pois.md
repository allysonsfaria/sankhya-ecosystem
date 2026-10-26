---
id: "9549625039255"
titulo: "Não é possível finalizar atividade, pois foi definido que essa atividade executa laudo e não existe nenhum laudo lançado para a mesma"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/9549625039255-N%C3%A3o-%C3%A9-poss%C3%ADvel-finalizar-atividade-pois-foi-definido-que-essa-atividade-executa-laudo-e-n%C3%A3o-existe-nenhum-laudo-lan%C3%A7ado-para-a-mesma"
trilha: "Solução de Problemas > Produção"
atualizado_em: "2026-07-22T15:07:29Z"
rotulos: ["Configuração", "Laudo", "Controle de Qualidade", "PROD_E00282", "Inclua e conclua o laudo necessário", "Falta de laudo em controle de qualidade", "Atividade requer laudo não lançado", "Erro", "Qualidade"]
---

# Não é possível finalizar atividade, pois foi definido que essa atividade executa laudo e não existe nenhum laudo lançado para a mesma

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/19297479221655) MENSAGEM:**

[PROD\_E00282] Não é possível finalizar atividade, pois foi definido que essa atividade executa laudo e não existe nenhum laudo lançado para a mesma.

**![Imagem 2: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/19297479230615) SITUAÇÃO:**

Ao criar um um processo com controle de qualidade e não inserir o laudo a mensagem é apresentada.

**![Imagem 3: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/19297451296535) CAUSA:**

Não incluir o laudo para a atividade CQ.

**![Imagem 4: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/19297451302423) SOLUÇÃO:**

Se a atividade Analise CQ estiver configurada para gerar o laudo, inclua o mesmo através do botão + e, de acordo com o resultado o laudo, será aprovado ou não.

![Imagem 5: Se a atividade Analise CQ estiver configurada para gerar o laudo, inclua o mesmo através do botão + e, de acordo com o…](https://ajuda.sankhya.com.br/hc/article_attachments/9549381625751)

Insira um novo laudo através do botão novo na tela. Após gerar e concluir o laudo, conseguirá salvar e finalizar a atividade com sucesso.

#### Laudo

Apenas as atividades configuradas com o tipo de operação igual a **"Laudo"** ou Amostragem + Laudo possuem acesso às funcionalidades existente na grade Laudo.

Na tela [Controle de Laudo de Amostras](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044611114), insira um novo laudo por meio do botão "Novo**"**; para isto, deve-se especificar o padrão de classificação do laudo em questão, de forma a sinalizar ao sistema qual o ensaio (teste) que deseja realizar neste momento. Automaticamente ao salvar o padrão de classificação, as características analisáveis do padrão são carregadas para que o usuário aponte seus respectivos resultados.

À medida em que são apontados os resultados das características, o sistema sinaliza com a cor **azul** para o que estiver dentro do aceitável e **vermelho** para o fora do aceitável.

Após a finalização do apontamento das diversas características, sinalize a conclusão do laudo (através do botão "Concluir **Laudo"**). O sistema considera sempre o último laudo de cada amostra como uma forma de permitir o lançamento de diversos laudos, porém, o último anula os demais como forma de correção de análises erradas anteriores.

Caso o Ciclo de Controle de Qualidade **"Permita aprovar laudos com ressalva"** e o padrão de classificação utilizado **"Permite confirmar quando laudo for rejeitado"**, então ao concluir um laudo no qual alguma das características analisáveis esteja fora do intervalo de aceitação, o sistema exibe uma mensagem questionando sobre a continuidade na aprovação do laudo mesmo assim (neste caso o resultado será Aprovado com Ressalva) ou então se o laudo será reprovado (o resultado será Reprovado).

Ao final de um Ciclo de Controle de Qualidade, representado pela passagem por uma atividade que **"Conclui Ciclo de Controle de Qualidade"**, serão consideradas todas as amostras para aquele produto/lote assim como os laudos das mesmas. Deste modo, finalize aquela instância de ciclo em questão e gere um resultado para mesma considerando o resultado do último laudo de cada amostra:

- **Se todos os laudos aprovados:** O resultado da Instância de Ciclo de Controle de Qualidade será **"Aprovado"**;
- **Se algum laudo for aprovado com ressalva:** Neste caso, o resultado da Instância do Ciclo de Controle de Qualidade será **"Aprovado com Ressalva"**;
- **Se algum laudo for reprovado:** Então o resultado da Instância do Ciclo de Controle de Qualidade será **"Reprovado"**.

[[voltar para o topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/9549625039255-N%C3%A3o-%C3%A9-poss%C3%ADvel-finalizar-atividade-pois-foi-definido-que-essa-atividade-executa-laudo-e-n%C3%A3o-existe-nenhum-laudo-lan%C3%A7ado-para-a-mesma#top)
