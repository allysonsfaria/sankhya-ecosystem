---
id: "11302265219351"
titulo: "Liberação de Filtros"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/11302265219351-Libera%C3%A7%C3%A3o-de-Filtros"
trilha: "Manual do Produto > Configurações e Cadastros > Configurações"
atualizado_em: "2026-07-29T13:40:17Z"
rotulos: ["Configuração", "Segurança", "Liberação de Filtros", "br.com.sankhya.mge.LiberacaoFiltros", "VALSEGFILTRO", "Controle de Acesso", "Governança de Filtros no Sankhya Om", "DPO", "Filtro Avançado"]
---

# Liberação de Filtros

```
![Imagem 1](https://ajuda.sankhya.com.br/hc/article_attachments/42310433362967) Módulo: Configurações > Controle de Acesso     ![Imagem 2](https://ajuda.sankhya.com.br/hc/article_attachments/42310463106839) Versão disponível: A partir da 4.20
```

---

Com o intuito de aprimorar a experiência dos usuários no **Sankhya Om**, essa ferramenta apresenta um recurso de filtros que simplifica a localização dos registros. Este recurso permite ao usuário aplicar filtros com base tanto nas informações presentes na tela quanto nas tabelas vinculadas à tela. Essa versatilidade pode abrir brechas para que analistas sem acesso direto as tabelas de ligação possam utilizar esses dados para aplicação de filtros, o que pode representar uma potencial fonte para vazamento de informações.

Para mitigar esse cenário e garantir uma governança mais robusta aos Encarregados de Proteção de Dados (DPOs), que precisam ter total visibilidade sobre as informações acessíveis aos usuários, implementamos esse recurso. Assim, sempre que um usuário sem permissões de acesso à entidade, como filtro avançado, solicitar a criação de um filtro que estabeleça ligação entre tabelas, será necessária intervenção para liberar essa ação.

Para ativar o recurso, é necessário habilitar o parâmetro **"Validação de segurança para filtros avançados - VALSEGFILTRO"**. Ao habilitá-lo, tanto os filtros criados para uso na interface do sistema quanto os filtros para uso na integração deverão ser analisados.

O procedimento de criação de filtros é explicado detalhadamente no artigo [Assistente de Filtros](https://ajuda.sankhya.com.br/hc/pt-br/articles/360062595693-Assistente-de-Filtros). A primeira etapa consiste em atribuir um nome ao filtro. Em seguida, é gerada a expressão a ser utilizada. Para expressões que estabelecem conexões entre entidades no sistema, o usuário será apresentado a um pop-up que solicitará o objetivo do filtro. Essa informação será encaminhada ao DPO, que, por meio do acesso a tela Liberação de Filtros, determinará se o filtro pode ser aplicado ou não.

![Imagem 3: O procedimento de criação de filtros é explicado detalhadamente no artigo Assistente de Filtros . A primeira etapa…](https://ajuda.sankhya.com.br/hc/article_attachments/17906901616791)

A fim de permitir que determinados usuários realizem filtros sem a necessidade de análise, é fundamental conceder o acesso à opção **"Filtro Avançado"** na tela em que o usuário irá utilizar. Essa permissão é concedida por meio da tela  [Acessos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044596854-Acessos) no **Sankhya Om**.

![Imagem 4: A fim de permitir que determinados usuários realizem filtros sem a necessidade de análise, é fundamental conceder o…](https://ajuda.sankhya.com.br/hc/article_attachments/19665271780503)

Após o usuário salvar a solicitação de filtro, os usuários que tiverem acesso à tela Liberação de Filtros receberão uma notificação indicando que existe um filtro aguardando a aprovação.

![Imagem 5: Após o usuário salvar a solicitação de filtro, os usuários que tiverem acesso à tela Liberação de Filtros receberão uma…](https://ajuda.sankhya.com.br/hc/article_attachments/17906545751831)

Ao acessar a tela, será possível avaliar a solicitação e determinar se o filtro é válido para utilização ou se requer ajustes prévios. Caso opte por reprovar o filtro, será fornecido o campo **"Motivo na Reprovação"** para que seja descrito uma orientação ao usuário que solicitou o filtro.

![Imagem 6: Ao acessar a tela, será possível avaliar a solicitação e determinar se o filtro é válido para utilização ou se requer…](https://ajuda.sankhya.com.br/hc/article_attachments/17962417534487)

Após a validação, o usuário que solicitou o filtro personalizado receberá uma notificação informando se a solicitação foi aprovada ou reprovada. Em caso de reprovação, o usuário não poderá aplicar o filtro e terá a opção de editá-lo para permitir uma nova avaliação por parte do DPO.
