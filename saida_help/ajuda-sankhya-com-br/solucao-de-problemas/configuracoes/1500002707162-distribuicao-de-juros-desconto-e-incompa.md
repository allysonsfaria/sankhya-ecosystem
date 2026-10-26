---
id: "1500002707162"
titulo: "Distribuição de Juros/Desconto é incompatível com Desconto por item, saiba mais"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/1500002707162-Distribui%C3%A7%C3%A3o-de-Juros-Desconto-%C3%A9-incompat%C3%ADvel-com-Desconto-por-item-saiba-mais"
trilha: "Solução de Problemas > Configurações"
atualizado_em: "2026-07-22T15:25:34Z"
rotulos: ["Configuração", "NF-e", "Juros", "Desconto", "Preferências", "Financeiro", "não apagar", "[CORE_E02347]", "#validadoPenelope", "Distribuição", "Erro"]
---

# Distribuição de Juros/Desconto é incompatível com Desconto por item, saiba mais

**![Imagem 1: MENSAGEM :](https://ajuda.sankhya.com.br/hc/article_attachments/16302510232983) MENSAGEM**:

[CORE\_E02347]: Distribuição de Juros/Desconto é incompatível com Desconto por item.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16302510233623) SOLUÇÃO:**

![Imagem 3: Escolha entre desabilitar o parâmetro "DISTJURO" , de acordo com sua necessidade de uso e compreendendo o funcionamento…](https://ajuda.sankhya.com.br/hc/article_attachments/16302560549527) Escolha entre **desabilitar o parâmetro** **"DISTJURO"**, de acordo com sua necessidade de uso e compreendendo o funcionamento desse, conforme detalhado abaixo, **ou refaça o lançamento inserindo o desconto exclusivamente pelo rodapé da nota**.

- Tela **"Preferências"**
- Chave: **"DISTJURO"**
- A documentação do Parâmetro DISTJURO quando está ativada habilita a opção de distribuir juros entre produtos, acessada através do menu Outras Opções, na tela de lançamento da Central de Atendimento ao Fornecedor e Cliente. Se não estiver ativada, a opção passa de "Distribuir Juros entre produtos" para "Distribuir Desconto entre produtos".
- **Com o parâmetro habilitado e inserindo desconto/juros no rodapé do lançamento**, o campo do item deve permanecer vazio, pois o sistema distribuirá o desconto/juros inserido no rodapé entre os itens e caso lá já haja valor lançado, ocorrerá o erro acima. Assim, o usuário deverá escolher entre desabilitar o parâmetro de acordo com sua necessidade de uso ou refazer o lançamento inserindo o desconto exclusivamente pelo rodapé.

**![Imagem 4: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16302560550551) CAUSA:**

 O incidente é um comportamento do sistema, ocorrendo no desconto dado por ITEM e pelo parâmetro DISTJURO estar ligado, de tal modo, ocorre a incompatibilidade. Pois, a documentação do presente  parâmetro exige que seja feito o desconto pelo rodapé e não pelos itens, utilizando assim o parâmetro **"DISTJDCONF"** para distribuir o desconto pelos itens na confirmação.
