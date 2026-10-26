---
id: "360044110214"
titulo: "Lock file has grown too large. Como resolver?"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044110214-Lock-file-has-grown-too-large-Como-resolver"
trilha: "Dúvidas Frequentes > Pessoal+"
atualizado_em: "2026-07-29T13:27:28Z"
rotulos: ["Configuração", "Relatórios", "Pessoal", "Folha de Pagamento", "Erro \"Lock file has grown too large\"", "Erro", "BDE"]
---

# Lock file has grown too large. Como resolver?

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16996120194455) MENSAGEM:**

Lock file has grown too large.

**![Imagem 2: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16996095353239) SITUAÇÃO:**

Ao acessar a rotina: Pessoal » Folha de Pagamento » Cálculo da folha » Cálculo da folha mensal e tentar efetuar o calculo da folha, em determinados momentos, ocorre a mensagem.

**![Imagem 3: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16996120196247) SOLUÇÃO:**

Para correção, siga os passos abaixo:

![Imagem 4: Acesse o aplicativo BDE na máquina local em que está ocorrendo o erro. Em seguida, acesse o diretório/pasta no qual…](https://ajuda.sankhya.com.br/hc/article_attachments/16996120199959) Acesse o aplicativo BDE na máquina local em que está ocorrendo o erro. Em seguida, acesse o diretório/pasta no qual está instalado o BDE: Exemplo: **C:\BDE**

Execute como Administrador o executável **bdeadmin.exe**

Aba: Configuration>>System>>INIT

**Localize** a opção: LOCAL SHARE e **altere** de TRUE para FALSE

Aba: Configuration>>Drivers>>Native>>PARADOX
**Localize** a opção: NET DIR e **insira** o valor: **C:\Users\%username%\temp**

**Salve** as alterações e **feche** o BDE.

![Imagem 5: Acesse o atalho do executável que está sendo utilizado e clique com o Botão Direito do mouse e acesse a opção:…](https://ajuda.sankhya.com.br/hc/article_attachments/16996095356823) Acesse o atalho do executável que está sendo utilizado e clique com o Botão Direito do mouse e acesse a opção: **"Propriedades".**

No campo **"Iniciar em"**, coloque: **C:\Temp\%username%\**

**Salve** a alteração e **acesse** normalmente o executável executando novamente o cálculo.

**![Imagem 6: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16996095361303) CAUSA:**

O erro ocorre quando há um grande processamento de dados ou as configurações do BDE estão inadequadas. O erro pode ocorrer em outras rotinas como Geração de Relatórios, Produção, Acesso ao Fast Service ou geração de notas. Então, este procedimento pode ser feito quando ocorrer o erro independente de qual rotina.

Lembrando que o procedimento deve ser feito em cada computador que acessa o sistema.
