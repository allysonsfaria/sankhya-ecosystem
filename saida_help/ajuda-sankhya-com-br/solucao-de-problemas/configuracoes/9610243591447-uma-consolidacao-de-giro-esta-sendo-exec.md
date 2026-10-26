---
id: "9610243591447"
titulo: "Uma consolidação de giro está sendo executada neste momento, tente novamente mais tarde."
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/9610243591447-Uma-consolida%C3%A7%C3%A3o-de-giro-est%C3%A1-sendo-executada-neste-momento-tente-novamente-mais-tarde"
trilha: "Solução de Problemas > Configurações"
atualizado_em: "2026-07-22T15:07:17Z"
rotulos: ["Configuração", "Análise de Giro", "Preferências", "Financeiro", "CORE_E05139", "Solução de problemas", "Parâmetro CALCMARLUCGIRO", "Consolidação de giro", "Erro"]
---

# Uma consolidação de giro está sendo executada neste momento, tente novamente mais tarde.

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/18864248216599) MENSAGEM:**

[CORE\_E05139]  Uma consolidação de giro está sendo executada neste momento, tente novamente mais tarde.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/18864248226711) SOLUÇÃO:**

![Imagem 3: Para que a execução da análise complete corretamente é necessário DESLIGAR o parâmetro CALCMARLUCGIRO , na tela…](https://ajuda.sankhya.com.br/hc/article_attachments/18864248235159) Para que a execução da análise complete corretamente é necessário DESLIGAR o parâmetro **CALCMARLUCGIRO**, na tela **Preferências** (Configurações » Avançado » Preferências), esse parâmetro tem como padrão DESLIGADO, caso tenha certeza da necessidade de utilização do parâmetro quem tem por função **"Calcular margem e lucro no consolidador de giro"** deve se atentar a 'performance' que esta relacionada ao "FILTRO",  definido na tela do agendador da analise, ou seja, se definimos um período grande (60,90 dias) a performance será comprometida, visto que o tempo de processamento será maior e o erro será apresentado.

![Imagem 4: Para que a execução da análise complete corretamente é necessário DESLIGAR o parâmetro CALCMARLUCGIRO , na tela…](https://ajuda.sankhya.com.br/hc/article_attachments/15768745558167)

![Imagem 5: Ao DESLIGAR o parâmetro basta reiniciar o sistema na tela Administrador do Servidor (Configurações » Avançado »…](https://ajuda.sankhya.com.br/hc/article_attachments/18864248236567) Ao DESLIGAR o parâmetro basta reiniciar o sistema na tela **Administrador do Servidor** (Configurações » Avançado » Administração do Servidor)  para que o job se destrave.

![Imagem 6: Ao DESLIGAR o parâmetro basta reiniciar o sistema na tela Administrador do Servidor (Configurações » Avançado »…](https://ajuda.sankhya.com.br/hc/article_attachments/15768568291991)

**![Imagem 7: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/18864289612439) CAUSA:**

Ocorre quando a consulta fica muito extensa e o parâmetro **CALCMARLUCGIRO**está ligado.
