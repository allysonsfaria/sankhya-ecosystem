---
id: "42427296924695"
titulo: "O que é a data de início da folha e como configurá-la?"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42427296924695-O-que-%C3%A9-a-data-de-in%C3%ADcio-da-folha-e-como-configur%C3%A1-la"
trilha: "PONTOTEL: Sistema de marcação de ponto > Cadastros"
atualizado_em: "2026-08-03T13:29:31Z"
rotulos: ["sync_hc", "pontotel", "pontotel_6a33edfa2e1913ce90dfeab6", "sync_hash_b269d20302a5"]
---

# O que é a data de início da folha e como configurá-la?

A data de início da folha é um dos parâmetros essenciais para a correta gestão dos registros de ponto no sistema Pontotel. Ela determina a partir de qual dia os apontamentos serão contabilizados na folha de ponto do colaborador, organizando o ciclo de fechamento e facilitando a conferência dos registros.

## Como funciona na prática?

Ao configurar a data de início da folha, você define o dia do mês em que a apuração da folha de ponto começa. A partir dessa data, o sistema passa a considerar todos os registros de ponto daquele colaborador para o novo ciclo da folha.

## Onde configurar a data de início da folha?

A data de início é definida dentro do **cadastro do empregado**. Portanto, atente-se na escolha do dia para cada colaborador, para que todos tenham a mesma data, a não ser que sua empresa realize o fechamento em períodos distintos.

![Imagem 1: A data de início é definida dentro do cadastro do empregado . Portanto, atente-se na escolha do dia para cada…](https://storage.crisp.chat/users/helpdesk/website/-/e/5/5/4/e554cdff9f2d480/461bff9d-dadb-4c3d-90e5-5effda_1hflvwr.png)

## Exemplos práticos

- Se a data de início da folha for definida para o dia 1, os registros de ponto serão contabilizados do primeiro ao último dia do mês.
- Caso a empresa opte por iniciar a folha em outra data, como dia 16, o ciclo de apuração será do dia 16 de um mês até o dia 15 do mês seguinte.

Essa flexibilidade é importante para empresas que desejam alinhar o fechamento da folha de ponto com datas específicas de pagamento, férias ou outros processos internos.

## Mudança de período na folha

Para colaboradores que já possuem uma folha criada, **não é recomendado** alterar o dia de início da folha, pois essa mudança irá desconfigurar os espelhos de ponto.
Caso a sua empresa precise ajustar o período de fechamento — seja por mudança na data de pagamento ou redução da folha no fim do ano, por exemplo — o procedimento correto é criar uma **folha de transição** com período customizado. A folha de transição atua como uma “quebra” no período atual da folha.

### Exemplo de como é realizada a configuração:

- Folha atual: **01 a 31**
- Folha de transição: **01 a 20**
- Nova folha: **21 a 20**
- Folhas seguintes: **21 a 20**

Nesse caso, se o período original era de 01 a 31 e você deseja alterar para 21 a 20, não deve ajustar diretamente a data de início no cadastro. Isso afetará todas as folhas destravadas, inclusive as já pagas, alterando o período de cálculo anterior.

Ao criar uma **folha de transição**, o histórico é preservado com os períodos antigos, e as próximas folhas passam a seguir o novo intervalo.

⚠️**Importante:**o período da folha de transição deve ser inferior a 30 dias para que o ajuste seja aplicado corretamente.

Se precisar realizar a mudança de período ou tiver dúvidas sobre o processo, entre em contato com o Suporte da Pontotel pelo [WhatsApp](https://api.whatsapp.com/send/?phone=551131852700&text&type=phone_number&app_absent=0) ou e-mail, abrindo um ticket na nossa [Central de Atendimento](https://sankhya.zendesk.com/hc/pt-br/articles/42427221575575). Estamos à disposição para te ajudar!
