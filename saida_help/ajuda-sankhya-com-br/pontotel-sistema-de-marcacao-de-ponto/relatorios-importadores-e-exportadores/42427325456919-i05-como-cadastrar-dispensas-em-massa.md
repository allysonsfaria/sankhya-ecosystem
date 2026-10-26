---
id: "42427325456919"
titulo: "I05 - Como cadastrar dispensas em massa"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42427325456919-I05-Como-cadastrar-dispensas-em-massa"
trilha: "PONTOTEL: Sistema de marcação de ponto > Relatórios, Importadores e Exportadores"
atualizado_em: "2026-08-03T13:29:33Z"
rotulos: ["sync_hc", "pontotel", "sync_hash_6ee23a67d558", "pontotel_6a33eddcd914e99c41d2a6d9"]
---

# I05 - Como cadastrar dispensas em massa

A funcionalidade de **Importação de Dispensas** foi criada para trazer mais agilidade e praticidade ao seu dia a dia operacional. Com ela, você consegue lançar dispensas de dia inteiro, parciais ou de múltiplos dias para diversos colaboradores simultaneamente, eliminando a necessidade de cadastros manuais individuais.

Neste artigo, você aprenderá:

- Como acessar o importador;
- Como preencher a planilha modelo;
- Como importar os dados para a plataforma;
- Regras e pontos de atenção.

---

## Como acessar e baixar a planilha modelo

1. No menu de navegação do [site Gestão](https://gestao.pontotel.com.br/), selecione a opção **Relatórios e Registros**.
2. Na lista de "importadores", selecione a opção **I05 - Importadores de arquivos.**
3. Preencha os **filtros** do importador

   - Em "tipo de importação", selecione a opção **Usuários.**

   ![Imagem 1: Em "tipo de importação", selecione a opção Usuários.](https://storage.crisp.chat/users/helpdesk/website/-/c/e/8/7/ce87d16ae4000000/image_1t74z3u.png)

- Logo abaixo, selecione a extensão do arquivo desejada para fazer o download da planilha modelo para preenchimento das informações.

![Imagem 2: Logo abaixo, selecione a extensão do arquivo desejada para fazer o download da planilha modelo para preenchimento das…](https://storage.crisp.chat/users/helpdesk/website/-/5/4/9/e/549e29d4eb740800/a5806108-0186-4c86-a771-c3b359_1xmi6kw.png)
> 💡 **Dica:** Escolha a extensão **.xlsx**. Ela é a mais segura, pois dispensa a configuração manual de células e evita erros na importação. O formato CSV não possui formatação visual e o antigo .xls exige ajustes que, se ignorados, podem desconfigurar seus dados.

---

## Como preencher a planilha modelo

A planilha é dividida em três seções principais para facilitar a organização. Abaixo, detalhamos os campos obrigatórios e opcionais.

1. **Informações da Dispensa (Campos obrigatórios de identificação e data)**
   Estes dados identificam quem receberá a dispensa e o motivo.

   - **Senha (PIN):** O identificador único do colaborador. Saiba mais sobre motivos padrão [neste artigo](https://sankhya.zendesk.com/hc/pt-br/articles/42427204716567).
   - **Motivo padrão:** Deve ser preenchido exatamente como cadastrado no sistema.
   - **Data da dispensa:** O dia em que a dispensa começa.
   - **Dias de dispensa:** Quantidade de dias. Se for maior que 1, o sistema considera como dispensa de múltiplos dias.

   ![Imagem 3: Dias de dispensa: Quantidade de dias. Se for maior que 1, o sistema considera como dispensa de múltiplos dias.](https://storage.crisp.chat/users/helpdesk/website/-/c/e/8/7/ce87d16ae4000000/image_10wf988.png)
2. **Informações da Dispensa (Configurações de horário para dispensas parciais)**
   Preencha estes campos **apenas** se a dispensa não for de dia inteiro.

   - **Parte do dia por intervalo (S/N):** Marque "S" se a dispensa for apenas por um período específico e não para o dia todo, e deseja inserir a data de início e término da dispensa, ao invés da sua duração total.
   - **Hora início:** Hora de ínicio da dispensa. Obrigatório caso seja uma dispensa parcial.
   - **Hora início é no dia seguinte? (S/N)**: Marque "S" se a dispensa inicia após a meia noite do dia de início da dispensa. Marque "S" apenas se deseja deseja adicionar a dispensa em um determinado dia, mas com os horários do dia seguinte.
   - **Hora fim:** Hora de término da dispensa. Obrigatório caso seja uma dispensa parcial.
   - **Hora fim é no dia seguinte? (S/N)**: Marque "S" apenas se a dispensa termina em um dia posterior à data inicial da dispensa, e se a dispensa for parcial.
   - **Parte do dia por duração (S/N)**: Marque "S" se a dispensa for apenas por um período específico e não para o dia todo, e deseja inserir sua duração total, ao invés da data de início e término da dispensa.
   - **Duração esperada da dispensa**: Preencha se for uma dispensa por duração (formato HH:MM).

   ![Imagem 4: Duração esperada da dispensa : Preencha se for uma dispensa por duração (formato HH:MM).](https://storage.crisp.chat/users/helpdesk/website/-/c/e/8/7/ce87d16ae4000000/image_1wglgpd.png)

> ⚠️ Atenção: Para dispensas parciais, deve ser escolhido o preenchimento por intervalo (hora de início e término da dispensa), ou duração (tempo total da dispensa). Dessa forma, será necessário preencher as colunas E a I para intervalo, ou colunas J e K para duração.

2. **Dados Médicos**
   Esses campos servem para enriquecer o registro, mas podem permanecer em branco caso não se apliquem. As colunas de L a U devem ser preenchidas com as informações do profissional responsável pelo atendimento decorrente da dispensa, como nome do profissional, classe, especialidade, CID, entre outros dados relevantes.

   ![Imagem 5: Dados Médicos Esses campos servem para enriquecer o registro, mas podem permanecer em branco caso não se apliquem. As…](https://storage.crisp.chat/users/helpdesk/website/-/c/e/8/7/ce87d16ae4000000/image_p5vga9.png)
3. **Configurações de cálculo**
   Aqui você define como essa dispensa vai impactar a folha de ponto. Se deixar em branco, o sistema usará a regra padrão já cadastrada no motivo.

   - **Duração esperada da pausa**: preencha este campo apenas em casos de dispensa parcial. Informe o tempo de pausa ao qual o colaborador tem direito, já considerando a dispensa. Atenção: este campo não se refere à pausa efetivamente realizada, mas sim à duração prevista ou esperada conforme o direito do colaborador.
   - **Descontar DSR (S/N):** Marque "S" se essa dispensa deve descontar o Descanso Semanal Remunerado.
   - **Ignorar jornadas de folga (S/N):** Marque "S" para que a dispensa não seja aplicada em dias que o colaborador já estaria de folga.
   - **Forma de cálculo:** Se quiser forçar uma regra específica para essa importação, você pode preencher com um dos três valores exatos abaixo. Caso não seja preenchido, será utilizado o valor padrão definido no motivo padrão usado na dispensa.
     - **descontar\_dispensa\_nas\_horas\_da\_jornada\_do\_dia**: Esta opção "neutraliza" as horas. O sistema entende que o colaborador não precisava trabalhar naquele período. As horas não são somadas como trabalhadas, mas também não são descontadas como falta. É como se a jornada daquele dia fosse reduzida.
     - **considerar\_como\_horas\_trabalhadas**: O sistema contabiliza aquele tempo de ausência como se o colaborador estivesse presente. Ou seja, essas horas entram positivamente no apontamento de "horas trabalhadas", garantindo que o dia seja computado integralmente.
     - **considerar\_como\_falta**: Utilizada quando a dispensa é registrada apenas para fins de histórico, mas o tempo deve ser descontado do colaborador. O sistema registra o período como uma ausência não justificada para fins de pagamento, gerando desconto no banco de horas ou na folha.

   ![Imagem 6: considerar_como_falta : Utilizada quando a dispensa é registrada apenas para fins de histórico, mas o tempo deve ser…](https://storage.crisp.chat/users/helpdesk/website/-/c/e/8/7/ce87d16ae4000000/image_1kdx16i.png)

> ⚠️ Atenção: Para garantir que sua importação ocorra sem inconsistências, fique atento a estas regras:

- **Dispensas Parciais:** O preenchimento dos horários de **início e fim** é obrigatório para dispensas por intervalo.
- **Campos não obrigatórios:** Se você não preencher campos opcionais (como dados médicos), o sistema irá ignorá-los ou usar as configurações padrão do motivo selecionado.
- **Limitações:**
  - Não é possível importar dispensas contendo **anexos** (arquivos de atestado digitalizados devem ser inseridos manualmente se necessário).
  - Não é possível editar as configurações dos motivos de dispensa através da planilha; ela serve apenas para lançar o registro.

---

## Como fazer o upload da planilha preenchida

1. Depois de preencher a planilha de acordo com o objetivo definido, salve o arquivo. Se estiver utilizando o programa Excel, clique em "Arquivo", e depois em "Salvar", ou aperte as teclas CTRL + S.
2. Retorne ao [site Gestão](https://gestao.pontotel.com.br/#/cognito/login), no mesmo local instruído no item 1, e selecione novamente a opção**I05 - Importadores de arquivos.** Clique no botão "**anexar**", e selecione o arquivo no seu computador com as informações preenchidas.

   ![Imagem 7: Retorne ao site Gestão , no mesmo local instruído no item 1, e selecione novamente a opção I05 - Importadores de…](https://storage.crisp.chat/users/helpdesk/website/-/c/e/8/7/ce87d16ae4000000/image_1kzbzu5.png)
3. Finalize clicando em **importar.**

   ![Imagem 8: Finalize clicando em importar.](https://storage.crisp.chat/users/helpdesk/website/-/c/e/8/7/ce87d16ae4000000/image_10zvhk1.png)
4. Aguarde o processo de importação da planilha ser finalizado.
5. Quando o processo for concluído, será gerado um relatório com o feedback da importação. Certifique-se de que as dispensas foram criadas.

---

Essa entrega representa um grande passo na automatização dos seus processos de RH, gerando ganhos significativos de produtividade.

Caso ainda tenha dúvidas ou precise de auxílio, entre em contato com o nosso time de Suporte pelo chat integrado ao [site Pontotel Gestão](https://gestao.pontotel.com.br/#/cognito/login) ou pelo [WhatsApp](https://api.whatsapp.com/send/?phone=551131852700&text&type=phone_number&app_absent=0)!
