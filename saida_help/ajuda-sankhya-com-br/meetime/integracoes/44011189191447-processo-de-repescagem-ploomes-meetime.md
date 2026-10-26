---
id: "44011189191447"
titulo: "Processo de repescagem Ploomes <> Meetime"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44011189191447-Processo-de-repescagem-Ploomes-Meetime"
trilha: "Meetime > Integrações"
atualizado_em: "2026-10-05T18:58:29Z"
rotulos: ["sync_hc", "meetime", "sync_hash_9ba16e72a4da", "meetime_1256"]
---

# Processo de repescagem Ploomes <> Meetime

## 1. O que é e para que serve?

Essa automação tem como objetivo facilitar o processo de repescagem de leads, permitindo que um contato seja retomado em uma data futura definida pelo time.

Para isso, tanto na Meetime quanto na Ploomes, utilizamos alguns campos personalizados que ajudam a transportar e organizar a informação da data de repescagem entre as duas plataformas.

De forma simples, o processo funciona assim:

1. A data de repescagem é informada na Meetime.
2. Essa informação é enviada para a Ploomes.
3. Na Ploomes, o valor recebido em um campo de texto é convertido para um campo de data.
4. A partir dessa data, o lead será redirecionado a Meetime para ser trabalhado novamente no momento certo.

Para facilitar, disponibilizamos abaixo um vídeo demonstrando todo o passo a passo das configurações desse processo:

[Configurações do processo de repescagem](http://loom.com/share/56b19392bb194862b6d8e459b0886ef2)

O vídeo mostra cada etapa de forma prática, ajudando na visualização das configurações necessárias.

Caso prefira, seguiremos com o passo a passo em formato escrito na sequência, com todas as orientações detalhadas para realizar a configuração.

## 2. Campos necessários para a automação

Para que o fluxo funcione corretamente, **precisamos criar três campos personalizados**, um na Meetime e dois na Ploomes.

### 2.1 Campo na Meetime

Na Meetime, será necessário criar um campo personalizado com as seguintes características

- **Nome sugerido:** Dia da Repescagem
- **Tipo:** Texto
- **Propriedades do campo:** Visível no formulário

![Imagem 1: Propriedades do campo: Visível no formulário](https://ajuda.sankhya.com.br/hc/article_attachments/44011207133591)

**⚠️ATENÇÃO⚠️**

**Esse campo será utilizado para registrar a data em que o lead deverá ser retomado. O preenchimento deve seguir o formato:**

**DD/MM/AAAA**

**Exemplo:**

**15/04/2026**

**Esse padrão é importante para garantir que a informação seja interpretada corretamente quando chegar na Ploomes.**

### 2.2 Campo na Ploomes

Na Ploomes será necessário criar 2 campos personalizados com as seguintes configurações:

- **Nome sugerido: Data da Repescagem (texto)**
- **Tipo: Texto**

![Imagem 2: Tipo: Texto](https://ajuda.sankhya.com.br/hc/article_attachments/44011210768919)

- **Nome sugerido: Data da Repescagem**
- **Tipo: Data**

![Imagem 3: Tipo: Data](https://ajuda.sankhya.com.br/hc/article_attachments/44011207470999)

Esse campo do tipo texto será responsável por receber a informação enviada pela Meetime por meio da integração.

A partir disso, vamos utilizar uma fórmula para transformar esse valor em uma data válida, que poderá ser usada nas automações dentro da própria Ploomes.

## 3. Conversão do texto para data na Ploomes

Quando a data chega na Ploomes como texto, é necessário convertê-la para um campo do tipo data.

Para isso, utilizamos uma fórmula em JavaScript que faz algumas validações antes de gerar o valor final. Essa fórmula garante que:

- o campo esteja preenchido corretamente
- o formato da data seja válido
- datas inexistentes (como 31/02) sejam evitadas
- o valor seja convertido para o formato aceito pelo sistema

A fórmula utilizada pode ser encontrada clicando [aqui](https://drive.google.com/file/d/1u38veytVd46E6CYtxw-FEcFv_RZg3CE_/view?usp=drive_link).

### 3.1 Criando a Automação

Com a fórmula em mãos, o próximo passo é criar uma automação geral (e não uma automação dentro do próprio campo).

Agora, acesse a página Administração, e vá até a seção Geral e procure por Automações:

![Imagem 4: Agora, acesse a página Administração, e vá até a seção Geral e procure por Automações:](https://ajuda.sankhya.com.br/hc/article_attachments/44011199324055)

Em seguida, na aba lateral esquerda, selecione a opção Card e clique em Nova automação:

![Imagem 5: Em seguida, na aba lateral esquerda, selecione a opção Card e clique em Nova automação:](https://ajuda.sankhya.com.br/hc/article_attachments/44011224372247)

Agora, é hora de configurar as regras da automação. Preencha da seguinte forma:

- Descrição: defina um nome para a automação
- Gatilho: selecione a opção Quando o item for editado e escolha o campo Data da Repescagem (Texto)
- Filtro: selecione o pipe (Card) onde o lead foi criado
- Ação da automação: escolha a opção Editar dados e selecione o campo Data da repescagem
- Tipo de preenchimento: selecione a opção Fórmula

Se tudo estiver configurado corretamente, a visualização da automação deve ficar conforme o esperado:

![Imagem 6: Se tudo estiver configurado corretamente, a visualização da automação deve ficar conforme o esperado:](https://ajuda.sankhya.com.br/hc/article_attachments/44011211453335)

### 3.2 Edição da fórmula

Neste ponto, é importante ter atenção ⚠️ ao configurar a fórmula.

Você deverá colar o código disponibilizado anteriormente no campo **Fórmula**.

Depois disso, vá até a linha 3 do código e substitua o conteúdo que está entre aspas ("") pelo campo **Data da repescagem (Texto)**, mantendo as aspas.

Após esse ajuste, a fórmula estará pronta para uso:

![Imagem 7: Após esse ajuste, a fórmula estará pronta para uso:](https://ajuda.sankhya.com.br/hc/article_attachments/44011226497303)

Você também pode utilizar a opção de teste da fórmula para visualizar como o campo irá se comportar quando o SDR preencher a data na Meetime:

![Imagem 8: Você também pode utilizar a opção de teste da fórmula para visualizar como o campo irá se comportar quando o SDR…](https://ajuda.sankhya.com.br/hc/article_attachments/44011224941335)

## 4. Automação da repescagem

Nesse tópico, vamos criar a automação responsável por retomar os leads na data definida.

Essa automação irá considerar os leads que tiveram a data preenchida na Meetime, passaram pela conversão na Ploomes e devem voltar ao fluxo na data correta.

Novamente, acesse a aba de Automações e crie uma nova automação do tipo Card.

Configure as regras da seguinte forma:

1. **Gatilho**: selecione a opção Periodicamente
2. **Execução**: defina para rodar diariamente (ou conforme a necessidade do seu processo)
3. **Filtro**:

   - motivo de perda igual a Repescagem
   - campo Data da repescagem com valor relativo como hoje ou esta semana
4. **Ação da automação**: selecione a opção Criar card

Nesse momento, você poderá escolher o pipe e o estágio de destino, além de definir quais campos serão preenchidos no novo card.

Se todas as etapas forem seguidas corretamente, a automação estará pronta e funcionando conforme esperado.

![Imagem 9: Se todas as etapas forem seguidas corretamente, a automação estará pronta e funcionando conforme esperado.](https://ajuda.sankhya.com.br/hc/article_attachments/44011200418455)

## 5. Configuração de automação por etapa

Por fim, com todas as configurações já realizadas, vamos definir o envio dos leads para a Meetime por meio da **Automação da Etapa** do pipe selecionado.

Essa configuração pode variar de acordo com a forma como o novo card foi preenchido. Abaixo, você pode conferir um exemplo de como essa estrutura pode ser configurada:

![Imagem 10: Essa configuração pode variar de acordo com a forma como o novo card foi preenchido. Abaixo, você pode conferir um…](https://ajuda.sankhya.com.br/hc/article_attachments/44011212212375)

Depois de configurar tudo, o processo passa a acontecer de forma simples no dia a dia. A data de repescagem é definida diretamente na Meetime e enviada automaticamente para a Ploomes. Ao chegar lá, a fórmula converte esse valor em uma data válida, permitindo que o lead seja retomado no momento certo, de forma organizada e sem a necessidade de controles manuais.

Ainda tem dúvidas? Entre em contato com a gente através do 
e-mail [suporte@meetime.com.br](mailto:suporte@meetime.com.br) ou WhatsApp através do número de telefone [(48) 3204-7590](https://wa.me/554832047590).
