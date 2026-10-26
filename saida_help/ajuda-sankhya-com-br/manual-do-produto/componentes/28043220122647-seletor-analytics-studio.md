---
id: "28043220122647"
titulo: "Seletor - Analytics Studio"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/28043220122647-Seletor-Analytics-Studio"
trilha: "Manual do Produto > Inteligência e Análise > Analytics AI > Componentes"
atualizado_em: "2026-09-23T17:14:55Z"
rotulos: ["Configuração", "Relatórios", "Filtros", "Componentes", "B.I.A - Business Intelligence Analyst", "Analytics AI", "Analytics Studio"]
---

# Seletor - Analytics Studio

O componente **"Seletor"** do [Analytics Studio](https://ajuda.sankhya.com.br/hc/pt-br/articles/25648251050647) permite que se apliquem filtros na tela de forma personalizada. Ele oferece várias opções de seleção, como, seleção única, múltipla, vertical, horizontal e seleção de data. Esse componente é ideal para criar filtros dinâmicos que permitem que cada cliente personalize a visualização dos dados conforme suas necessidades.

![Imagem 1: O componente "Seletor" do Analytics Studio permite que se apliquem filtros na tela de forma personalizada. Ele oferece…](https://ajuda.sankhya.com.br/hc/article_attachments/28043245034775)

Para configurar o componente Seletor, siga os passos abaixo:

1. Arraste o componente Seletor para a tela onde deseja aplicar o filtro;
2. Escolha o cadastro que será usado para preencher as opções do Seletor;
3. Selecione o tipo de Seletor que deseja utilizar, dentre as seguintes opções:

   - **Seleção Única:** permite selecionar apenas uma opção.
   - **Seleção Múltipla:** permite selecionar várias opções.
   - **Vertical:** exibe as opções em uma lista vertical.
   - **Horizontal:** apresenta as opções em uma lista horizontal.
   - **Seleção de Data:** permite selecionar uma data específica ou um intervalo de datas, oferecendo um filtro de range de datas onde o usuário pode definir uma data inicial e final.

[Vídeo: tutorial do artigo](https://www.youtube.com/watch?v=D1X_kkXryaI)

O componente Seletor filtra suas opções com base nos critérios dos filtros que foram salvos na tela. Vale destacar que essa filtragem é exclusiva para o seletor em questão e não interfere nos demais seletores presentes na tela.

[Vídeo: tutorial do artigo](https://www.youtube.com/watch?v=5BG8xa2BLgo)

**Mostrar Título:** ativa ou desativa a exibição do título do Seletor.

**Limitar Registros:** caso queira que as opções do Seletor estejam filtradas, utilize essa opção.

**Reatividade Manual:** se o seu Seletor deveria afetar um componente SQL e não está afetando, será pelo fato de não ter vinculado algum cadastro à VIEW de SQL. Isso não é um problema, pois poderá configurar a reatividade manual em um seletor, o fazendo atualizar um componente específico sempre que ele for alterado.
