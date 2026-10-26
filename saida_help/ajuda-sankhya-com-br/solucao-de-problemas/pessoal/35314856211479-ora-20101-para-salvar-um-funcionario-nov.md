---
id: "35314856211479"
titulo: "ORA-20101: Para salvar um funcionário novo com vínculo de prazo indeterminado selecione a opção *Dispensado do período de experiência"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/35314856211479-ORA-20101-Para-salvar-um-funcion%C3%A1rio-novo-com-v%C3%ADnculo-de-prazo-indeterminado-selecione-a-op%C3%A7%C3%A3o-Dispensado-do-per%C3%ADodo-de-experi%C3%AAncia"
trilha: "Solução de Problemas > Pessoal+"
atualizado_em: "2026-07-29T13:20:51Z"
rotulos: ["Funcionários", "eSocial", "ORA-20101", "ORA-06512", "Central do eSocial", "Cadastro", "Erro", "ORA-2010", "ORA-04088: erro durante a execução do gatilho 'SANKHYA.TRG_VINCULOS_TFPFUN'", "Para salvar um funcionário novo com vínculo de prazo indeterminado", "selecione a opção *Dispensado do período de experiência*", "ORA-06512: em \"SANKHYA.TRG_VINCULOS_TFPFUN\" line 18"]
---

# ORA-20101: Para salvar um funcionário novo com vínculo de prazo indeterminado selecione a opção *Dispensado do período de experiência

**MENSAGEM**

ORA-20101: Para salvar um funcionário novo com vínculo de prazo indeterminado selecione a opção \*Dispensado do período de experiência\*
ORA-06512: em "SANKHYA.TRG\_VINCULOS\_TFPFUN", line 18
ORA-04088: erro durante a execução do gatilho 'SANKHYA.TRG\_VINCULOS\_TFPFUN'

**SITUAÇÃO**

Durante a **admissão de um novo colaborador** no sistema, ao tentar salvar o cadastro do funcionário, a mensagem de erro é apresentada. Isso ocorre quando o usuário seleciona um **tipo de vínculo inadequado** para a situação do funcionário que está sendo cadastrado.

**SOLUÇÃO**

**(1)** Acesse o cadastro do funcionário e verifique o **tipo de vínculo** selecionado.

**(2)** Se o funcionário está entrando em **contrato de experiência**, selecione o vínculo de **prazo determinado**.

![Imagem 1: (1) Acesse o cadastro do funcionário e verifique o tipo de vínculo selecionado. (2) Se o funcionário está entrando em…](https://ajuda.sankhya.com.br/hc/article_attachments/35628382494743)

**(3)** Utilize a opção **"Dispensado do período de experiência"** apenas quando:
• O colaborador já tiver cumprido os 90 dias de experiência em contrato anterior
• For contratado diretamente em prazo indeterminado (casos específicos permitidos pela CLT)

**(4)** Salve o cadastro após realizar os ajustes necessários.

**CAUSA**

O erro ocorre porque foi selecionada a opção de vínculo **"10 – Prazo indeterminado pessoa jurídica"** para um funcionário **pessoa física**, cuja contratação deve obedecer às regras da **CLT**. Segundo a legislação trabalhista, novos colaboradores contratados sob o regime da CLT devem inicialmente passar pelo **contrato de experiência** de até **90 dias**, configurando vínculo **por prazo determinado**. Somente após a conclusão do período de experiência é que o vínculo pode ser efetivado como **prazo indeterminado**.
