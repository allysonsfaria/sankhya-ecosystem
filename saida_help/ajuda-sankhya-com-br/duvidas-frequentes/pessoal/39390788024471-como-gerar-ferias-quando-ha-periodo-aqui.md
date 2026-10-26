---
id: "39390788024471"
titulo: "Como gerar férias quando há período aquisitivo vencido e proporcional simultaneamente?"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/39390788024471-Como-gerar-f%C3%A9rias-quando-h%C3%A1-per%C3%ADodo-aquisitivo-vencido-e-proporcional-simultaneamente"
trilha: "Dúvidas Frequentes > Pessoal+"
atualizado_em: "2026-09-18T11:22:27Z"
rotulos: ["Configuração", "Requisições", "Folha de Pagamento", "Férias", "Artigo criado KCS", "Sankhya RH - KCS", "Período Aquisitivo"]
---

# Como gerar férias quando há período aquisitivo vencido e proporcional simultaneamente?

Quando um colaborador possui um **período aquisitivo vencido** e outro **proporcional em andamento**, é comum surgirem dúvidas sobre como proceder com o cálculo e a geração das férias restantes. Este artigo explica como o sistema Sankhya trata essa situação e orienta sobre os procedimentos corretos.

### Entendendo os períodos aquisitivos

O **período aquisitivo** corresponde aos 12 meses trabalhados que geram o direito a 30 dias de férias. Cada mês completo trabalhado equivale a **1 avo**, que representa 2,5 dias de férias. Quando o colaborador completa 12 avos, ele adquire o direito aos 30 dias completos.

É possível que o colaborador tenha **férias vencidas** (de um período aquisitivo já completo) e, simultaneamente, esteja acumulando **férias proporcionais** de um novo período aquisitivo em andamento.

### Verificando os períodos aquisitivos no sistema

Antes de gerar as férias restantes, verifique os períodos aquisitivos cadastrados para o funcionário no sistema. Siga os passos abaixo:

**(1)** Acesse a tela **"Requisição" (Pessoal+ » Rotinas Folha » Requisições)** clique no card de "**Férias**".

**(2)** Selecione a empresa e o departamento e em seguida localize o funcionário desejado e selecione-o.

**(3)** Clique no botão **"Aquisitivo"** para consultar os períodos aquisitivos cadastrados.

**(4)** Verifique se ainda existe saldo de férias pendente no período aquisitivo vencido (2024–2025). O próximo período aquisitivo (2025–2026) somente será disponibilizado após a quitação integral do saldo existente no período anterior.

[GIF animado: Imagem 1: (1) Acesse a tela "Requisição" (Pessoal+ » Rotinas Folha » Requisições) clique no card de " Férias ". (2) Selecione a…](https://ajuda.sankhya.com.br/hc/article_attachments/41051557178647)

### Gerando os dias restantes de férias

Para gerar os 15 dias restantes do período aquisitivo vencido (2024–2025), verifique se já existe uma sequência de férias cadastrada para esse período. Caso não exista, crie uma nova sequência de férias vinculada ao mesmo período aquisitivo. Siga os passos abaixo:

**(1)** Na rotina de Requisição, no card de Férias, após selecionar o colaborador, acesse a aba **"Aquisitivos"**.

**(2)** Localize o período aquisitivo 2024-2025 que possui saldo de dias restantes.

![Imagem 2: (2) Localize o período aquisitivo 2024-2025 que possui saldo de dias restantes.](https://ajuda.sankhya.com.br/hc/article_attachments/41051557180183)

**(3)** Crie uma **"Sequência 2"** para esse mesmo período aquisitivo, informando a data de início das férias e a quantidade de dias.

![Imagem 3: (3) Crie uma "Sequência 2" para esse mesmo período aquisitivo, informando a data de início das férias e a quantidade de…](https://ajuda.sankhya.com.br/hc/article_attachments/41051583839639)

**(4)** Confirme que a **"Data de início do período aquisitivo"** na sequência 2 seja igual à data da sequência 1 desse mesmo período.

![Imagem 4: Salve as alterações e proceda com o cálculo da folha de férias.](https://ajuda.sankhya.com.br/hc/article_attachments/41051583840023)

**(5)** Salve as alterações e proceda com o cálculo da folha de férias.

### Atenção aos requisitos do sistema

O sistema Sankhya possui uma validação importante: a segunda ou terceira sequência de férias só pode ser inserida quando a **"Data de início do período aquisitivo"** for igual à data da sequência 1 desse período. Isso garante que as férias fracionadas estejam vinculadas ao mesmo período aquisitivo.

Caso o sistema apresente mensagem de erro ao tentar criar a sequência 2, verifique se:

- A **"Data de início do período aquisitivo"** está correta. Lembrando que ele não deixa incluir a data de saída nessa rotina.
- O período aquisitivo anterior foi corretamente importado ou calculado no sistema.

### Considerações sobre férias coletivas

Quando o colaborador participa de férias coletivas e possui menos de um ano de empresa, o sistema pode abrir um novo período aquisitivo automaticamente, dependendo da configuração da marcação **"Mantém Períodos Aquisitivos em Férias"**.

Para saber mais sobre férias coletiva basta acessar o artigo: [**Cálculo de férias coletivas**](https://ajuda.sankhya.com.br/hc/pt-br/articles/17266680029335-C%C3%A1lculo-de-f%C3%A9rias-coletivas)
