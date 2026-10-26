---
id: "35835468147735"
titulo: "Perguntas Frequentes sobre o Crédito do trabalhador"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/35835468147735-Perguntas-Frequentes-sobre-o-Cr%C3%A9dito-do-trabalhador"
trilha: "Manual do Produto > Pessoas+ > Crédito do Trabalhador"
atualizado_em: "2026-09-27T18:48:24Z"
rotulos: ["MGE", "Crédito", "Folha", "eSocial", "Configuração Funcionários", "eConsignado", "Crédito do trabalhador (eConsignado)", "Pessoal+"]
---

# Perguntas Frequentes sobre o Crédito do trabalhador

**1. A partir de quais versões do sistema a implementação do crédito do trabalhador está disponível?**

O crédito do trabalhador está disponível a partir das seguintes versões:

- **Pessoal+**: 5.31 / San 3.11
- **MGE**: 4.65.05 - Para o MGE, é necessário atualizar o banco de dados para a mesma versão do executável.

**2. Já houve workshop realizado sobre Crédito do trabalhador?**

Sim. O primeiro workshop ocorreu no dia 19/05. Abaixo, os links dos materiais apresentados:

- [eConsignado no Pessoal+ – Workshop 19/05/2025](https://drive.google.com/file/d/1fhrVc7fs7tOtMfJNxZownDNN5nGXsH7M/view)
- [Cópia da apresentação – Crédito do Trabalhador](https://docs.google.com/presentation/d/1woUu9j5SDbHZGP0w_hK80F7UowbEPmBbiEL_HSNXtRo/edit?slide=id.g356b8d85171_0_64#slide=id.g356b8d85171_0_64)

**3. Onde acessar a planilha com as informações de empréstimo?**

Entre os dias 21 e 25, além da notificação via DET, os dados das consignações estarão disponíveis no **Portal Emprega Brasil**, permitindo o acesso das empresas para correta escrituração dos descontos em folha.

| ![Imagem 1: Entre os dias 21 e 25, além da notificação via DET, os dados das consignações estarão disponíveis no Portal Emprega…](https://ajuda.sankhya.com.br/hc/article_attachments/42310437438743) | ![Imagem 2: Entre os dias 21 e 25, além da notificação via DET, os dados das consignações estarão disponíveis no Portal Emprega…](https://ajuda.sankhya.com.br/hc/article_attachments/42310437441047) |
| --- | --- |

**4. Qual é a margem consignável para o empréstimo?**

O trabalhador poderá comprometer até **35% do salário** com as parcelas do empréstimo.

**5. Em quais tipos de folha ocorrerá o desconto?**

O desconto ocorrerá nas **folhas mensais e de rescisão**, conforme a **Portaria MTE nº 435/2025**.

**6. Terá provisão para férias e para adiantamento?**

Sim. A provisão já está implementada para a folha de **férias**, e a de **adiantamento** está prevista para junho.

![Imagem 3: Sim. A provisão já está implementada para a folha de férias , e a de adiantamento está prevista para junho.](https://ajuda.sankhya.com.br/hc/article_attachments/35835468142743)

**7. O que será considerado para o cálculo da margem consignável?**

A margem consignável utilizada para cálculo inicial do empréstimo representa o limite máximo de desconto mensal permitido no momento da contratação do empréstimo, que correspondente a 35% da remuneração disponível. Conforme a Portaria MTE nº 435/2025, a remuneração disponível para o cálculo da margem consignável é composta pelo somatório das rubricas de vencimento com incidência de contribuição previdenciária, subtraindo-se:

- rubricas de desconto com incidência previdenciária;
- desconto da contribuição previdenciária do trabalhador;
- IRRF;
- outros descontos compulsórios.

O sistema realiza esse cálculo automaticamente, desde que os eventos usados sejam os **padrões**. Eventos como premiações, transportes, diárias de viagem, dentre outros, **não entram** nesse cálculo.

[Acesse o manual oficial para mais detalhes.](https://www.gov.br/trabalho-e-emprego/pt-br/assuntos/credito-do-trabalhador/empregador/manual-operacional-do-empregador-credito-do-trabalhador-v2-16-05-25.pdf)

**8. Quais eventos estão sendo considerados para o cálculo da margem consignável de 35%?**

Eventos com incidência de **INSS**, como: salário base, periculosidade, insalubridade, hora extra, DSR, adicional noturno, férias etc.

São descontados: INSS, IRRF e faltas.

[Mais detalhes no manual oficial](https://www.gov.br/trabalho-e-emprego/pt-br/assuntos/credito-do-trabalhador/empregador/manual-operacional-do-empregador-credito-do-trabalhador-v2-16-05-25.pdf)

**9. Como será realizado o lançamento no sistema?**

No **Pessoal+**, o lançamento pode ser feito:

- Via **importador** na tela **Lançamento de Movimento**;
- Ou **manualmente**, como movimento mensal ou de rescisão.

**Observação:** a importação **não está disponível para o MGE**.

**10. Quais eventos do sistema estão relacionados ao Crédito do Trabalhador?**

Os principais eventos são:

- **Desconto Crédito Trabalhador**: evento padrão enviado ao eSocial com valor exato do desconto realizado em folha, considerando a margem consignável. Desconto efetivo da parcela.
- **Base Margem Créd. Trabalhador**: base do cálculo para a margem consignável.
- Cred. do Trabalhador: valor da parcela do crédito do trabalhador sem considerar a margem consignável, ou seja, o montante que deveria ser descontado.
- **Parcela Não Descont. Cred. Trab.**: responsável por retornar o valor não descontado do trabalhador quando não há margem consignável suficiente para quitação total da parcela.
- **Prov. Cred. Trabalhador**: esse evento é responsável por provisionar o desconto do crédito do trabalhador na folha de férias.
- **Ressarc. Cred. Trab. Ferias**: o evento é responsável por ressarcir a provisão do desconto do crédito do trabalhador feito na folha de férias.

**Observações:**

- ao atualizar as fórmulas e eventos no Pessoal+, os novos eventos padrão criados podem não utilizar os mesmos códigos apresentados nas documentações, pois esses códigos podem já estar em uso na base do cliente;
- para o MGE será necessário que o usuário crie os eventos manualmente conforme documentação na Central de Ajuda, devido à impossibilidade de subir de forma automática via banco para todos os clientes.

**11. Como será provisionado o valor do Crédito do Trabalhador nas férias?**

O sistema irá utilizar o evento **PROVCREDTRABFERIAS**, que será responsável por calcular o valor da provisão considerando os dias de férias trabalhados. Após as férias, quando calcular a folha mensal, o evento **RESSARCPROVCREDTRAB** será responsável por ressarcir a provisão na folha, devolvendo o valor para os proventos, enquanto o evento **DESCCREDTRABALHADOR** fará o desconto efetivo da parcela.

**12. Como será a apresentação no holerite? Terá mensagem informativa se não houver desconto?**

- no **Pessoal+**, via importador, o holerite exibirá uma subseção com informações do empréstimo originadas da planilha disponibilizada pelo governo.
- no **lançamento manual** (Pessoal+ ou MGE), serão mostrados também: número do contrato, valor da parcela e banco.

Se o valor não for descontado em qualquer desses produtos, aparecerá a seguinte mensagem:

**"Atenção!**

**Não foi possível efetuar o desconto, total ou parcial, referente ao seu empréstimo ‘crédito do trabalhador’, pois o valor ultrapassa o limite de 35% da remuneração disponível, conforme a Lei nº 10.820/2003 e Portaria MTE nº 435/2025. Por favor, entre em contato com a sua instituição financeira para regularizar o pagamento."**

**13. Será necessário realizar o cadastro individual dos bancos no Pessoal+?**

Ossistemas, **Pessoal+** e **MGE** já trazem os bancos cadastrados conforme o Bacen. Se a instituição não for encontrada, o cadastro deverá ser feito na tela **Bancos**.

**14. Pode ser feito o desconto integral do empréstimo na rescisão?**

![Imagem 4: 14. Pode ser feito o desconto integral do empréstimo na rescisão?](https://ajuda.sankhya.com.br/hc/article_attachments/35835468144151)

[Consulte o manual oficial para essa situação específica](https://www.gov.br/trabalho-e-emprego/pt-br/assuntos/credito-do-trabalhador/empregador/manual-operacional-do-empregador-credito-do-trabalhador-v2-16-05-25.pdf)

**15. Lancei os empréstimos no movimento, mas o evento de desconto não aparece na folha. O que pode ter acontecido?**

Pode ser que **eventos padrão (que fazem parte da base de margem do crédito do trabalhador) estejam desprotegidos**, o que impede o vínculo correto com a base de margem.

Recomendações:

- **não desproteger** eventos padrão.
- se usar eventos personalizados, certifique-se de que estejam vinculados à base de margem do crédito do trabalhador. Isso é essencial para que o desconto do crédito funcione corretamente.

**16. Como funciona o processo para empresas com matriz e filiais?**

As informações dos colaboradores da **matriz e filiais** virão em **um único arquivo** do Portal Emprega Brasil, que será importado no sistema.

Quer saber mais, acesse as [Perguntas Frequentes do Ministério do Trabalho e Emprego](https://www.gov.br/trabalho-e-emprego/pt-br/assuntos/credito-do-trabalhador/perguntas-frequentes/perguntas-frequentes/).
