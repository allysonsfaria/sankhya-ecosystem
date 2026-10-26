---
id: "42427235649175"
titulo: "I06 - Como utilizar o Importador de Banco de Horas"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42427235649175-I06-Como-utilizar-o-Importador-de-Banco-de-Horas"
trilha: "PONTOTEL: Sistema de marcação de ponto > Relatórios, Importadores e Exportadores"
atualizado_em: "2026-08-03T12:51:14Z"
rotulos: ["sync_hc", "pontotel_6a332859bdb29e2882d990bb", "sync_hash_ac800906bcb4", "pontotel"]
---

# I06 - Como utilizar o Importador de Banco de Horas

O **Importador de Banco de Horas** (I06) permite que gestores façam a atualização do saldo de banco de horas dos colaboradores de forma rápida e prática, por meio de uma planilha em formato **.xlsx**.
Essa funcionalidade é ideal para empresas que precisam registrar ou ajustar grandes volumes de dados de forma centralizada, sem a necessidade de lançar manualmente colaborador por colaborador.

Neste artigo, você aprenderá como fazer a importação de banco de horas através de planilha.

---

## Como utilizar o Importador de Banco de Horas

1. No menu de navegação do [site Gestão](https://gestao.pontotel.com.br/), selecione a opção **Relatórios e Registros**.
2. Vá até a seção **Importações** e selecione **I06 - Importador de Banco de Horas**
3. Em "tipo de importação", selecione a opção **"Banco de horas"**.
4. Clique em "**baixar em xlxs"** para fazer o download da planilha padrão que deverá ser preenchida.

   ![Imagem 1: Clique em " baixar em xlxs" para fazer o download da planilha padrão que deverá ser preenchida.](https://storage.crisp.chat/users/helpdesk/website/-/c/e/8/7/ce87d16ae4000000/image_ok7dtj.png)
5. **Preencha a planilha modelo**

![Imagem 2: Preencha a planilha modelo](https://storage.crisp.chat/users/helpdesk/website/-/c/e/8/7/ce87d16ae4000000/image_v1qnys.png)

**5.1.**Informe os campos **SENHA, NOME,CPF**ou**PIS**no formato de texto simples (Colunas **A** a**D**), exatamente como está no cadastro do empregado.

> ⚠️ Atenção: Se preencher o CPF, não preencha o PIS. Caso preencha o PIS, mantenha o CPF em branco. Apenas um dos campos deve ser preenchido.

**5.2.** Utilize o formato decimal com ponto (.) para os campos **Total Positivo** e **Total Negativo**(Colunas **E** e**F**)

- Exemplo: `0.5` representa **00:30**
- Exemplo: `1.0` representa **01:00**
- Exemplo: `1.5` representa **01:305.3**. Preencha a data que o saldo será lançado no formato **DD/MM/AAAA** (Colunas **G** a **I**)

**5.4.** Caso haja horas extras, horas extraordinárias e/ou horas especiais, some os valores para que correspondam ao **Total Positivo**.

- Exemplo:
  - Hora extra: `1.0`
  - Hora extra extraordinária: `1.0`
  - Hora extra especial: `1.0`
  - Total Positivo: `3.0`

**5.5.** Se o saldo que será adicionado deve ser considerado para cálculo de **limites de banco** (Coluna M), preencha com "S" ou mantenha em branco. Caso não deva ser considerado, preencha com "N".

**5.6.** Caso seja uma **baixa parcial** do saldo de banco de horas do colaborador (Coluna **N**), preencha com "S".

> 💡 Dica: Utilize [este site](https://www.calculadora-online.xyz/conversao-hora-minuto-decimal) para fazer a conversão de horas e minutos para o formato decimal.

6. Após preencher, salve a planilha. volte na tela do importador e clique no ícone abaixo para selecionar o arquivo no computador.

   ![Imagem 3: Após preencher, salve a planilha. volte na tela do importador e clique no ícone abaixo para selecionar o arquivo no…](https://storage.crisp.chat/users/helpdesk/website/-/c/e/8/7/ce87d16ae4000000/image_q6hd4k.png)
7. Clique em **"importar"** para fazer o upload do arquivo.

   ![Imagem 4: Clique em "importar" para fazer o upload do arquivo.](https://storage.crisp.chat/users/helpdesk/website/-/c/e/8/7/ce87d16ae4000000/image_1vp1je3.png)
8. Aguarde o processo de importação da planilha ser finalizado.
9. Quando o processo for concluído, será gerado um relatório com o feedback da importação.
10. Certifique-se de que o saldo de banco de horas foi inserido na folha de ponto do colaborador, e está sendo computado no acumulado do banco de horas.

---

> Observações:

- Os dados informados na planilha precisam estar **exatamente iguais** aos cadastrados no sistema (como CPF e nome), caso contrário a importação poderá falhar.
- Sempre revise os valores antes de importar, garantindo que a soma dos campos de hora extra corresponda ao **Total Positivo** informado.
- O formato decimal com ponto (.) é obrigatório. Vírgulas (,) não serão aceitas.
- Guarde uma cópia da planilha importada para controle interno ou auditoria.

---

O Importador de Banco de Horas (I06) oferece mais agilidade e eficiência na gestão de horas, permitindo que ajustes sejam feitos em lote de forma simples e segura. Seguindo corretamente o preenchimento da planilha modelo e os passos acima, você garante que as informações sejam importadas sem erros.

Caso ainda tenha dúvidas ou precise de auxílio, entre em contato com o nosso time de Suporte pelo chat integrado ao [site Pontotel Gestão](https://gestao.pontotel.com.br/#/cognito/login) ou pelo [WhatsApp](https://api.whatsapp.com/send/?phone=551131852700&text&type=phone_number&app_absent=0)!
