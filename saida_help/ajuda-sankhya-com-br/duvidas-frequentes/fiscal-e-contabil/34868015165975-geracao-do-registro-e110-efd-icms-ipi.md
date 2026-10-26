---
id: "34868015165975"
titulo: "Geração do registro E110 - EFD ICMS/IPI"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/34868015165975-Gera%C3%A7%C3%A3o-do-registro-E110-EFD-ICMS-IPI"
trilha: "Dúvidas Frequentes > Fiscal e Contábil"
atualizado_em: "2026-07-22T14:26:32Z"
rotulos: ["Configuração", "Fiscal", "Ajuste da Apuração de ICMS e ICMS ST", "Cadastro Livro ICMS/IPI", "SEFAZ", "ICMS", "Impostos", "EFD", "Geração do registro E110 - EFD ICMS/IPI", "Registro de Apuração de ICMS", "registro E110"]
---

# Geração do registro E110 - EFD ICMS/IPI

O registro E110 no SPED Fiscal reúne os valores apurados de ICMS e ICMS-ST em determinado período, consolidando débitos, créditos e saldos a transportar. Ele é fundamental para a escrituração correta e para garantir a consistência das informações fiscais.

Confira as regras sistêmicas para a geração dele na aplicação SankhyaOm:

**(1)** **Campo 2 - VL\_TOT\_DEBITOS:**

Quando executamos a Rotina **"Registro de Apuração de ICMS"** o sistema constrói os valores de débitos das notas dos livros fiscais e serão esses os valores levados para esse campo.

**(1)** **Campo 3 - VL\_AJ\_DEBITOS:**

Todos ajustes lançados na tela **"Ajuste da Apuração de ICMS e ICMS ST"** com o tipo de apuração **"Débito"** e os ajustes lançados na tela **"Cadastro Livro ICMS/IPI",** na aba **"Ajustes de Documentos - EFD Fiscal",** com código que é pertinente a débito, o sistema somará e apresentará no campo.

(1)** Campo 4 - VL\_TOT\_AJ\_DEBITOS:**

Os ajustes lançados na tela Ajuste da Apuração de ICMS e ICMS ST com o campo Tipo apuração igual a 'Outros débitos'.

(1)** Campo 5 - VL\_ESTORNOS\_CRED:**

Os ajustes lançados na tela Ajuste da Apuração de ICMS e ICMS ST com o campo Tipo apuração igual a **"Estorno de Créditos"**.

(1)** Campo 6 - VL\_TOT\_CREDITOS:**

Será o total dos lançamentos feitos na tela **"Cadastro Livro ICMS/IPI"** como entrada e que tenha valor de ICMS neste tela.

(1)** Campo 7 - VL\_AJ\_CREDITOS:**

Será o total dos lançamentos feitos na tela Cadastro Livro ICMS/IPI e que tenham os ajustes lançados na aba 'Ajustes de Documentos - EFD Fiscal'.

**Observação**: a aplicação segue as regras dispostas no guia prático, para esse campo, analisando o código do ajuste usado.

(1)** Campo 8 - VL\_TOT\_AJ\_CREDITOS:**

Os ajustes lançados na tela Ajuste da Apuração de ICMS e ICMS ST com o campo Tipo apuração igual a **Outros Créditos**.

(1)** Campo 9 - VL\_ESTORNOS\_DEB:**

Os ajustes lançados na tela Ajuste da Apuração de ICMS e ICMS ST com o campo "Tipo apuração" igual a 'Estorno de débitos'.

(1)** Campo 10 - VL\_SLD\_CREDOR\_ANT:**

Será levado o que estiver no campo **'Saldo Credor Ant.'** da tela de Registro de Apuração ICMS.

(1)** Campo 11 - VL\_SLD\_APURADO:**

Será o resultado da seguinte equação:

campo 2 + campo 3 + campo 4 + campo 5 - campo 6 - campo 7 - campo 8 - campo 9 - campo 10

se o cálculo for negativo, o valor será zerado.

(1)** Campo 12 - VL\_TOT\_DED:**

Os ajustes lançados na tela Ajuste da Apuração de ICMS e ICMS ST com o campo Tipo apuração igual a **"Deduções do imposto apurado"** somando com todos os registro lançados no C197 e filhos do C800 (gerados pela aplicação) somados, respeitando as regras do guia prático sobre os códigos de ajustes.

(1)** Campo 13 - VL\_ICMS\_RECOLHER:**

Será a diferença entre o campo 11 - 12. Caso o valor dê negativo, o sistema vai zerar o valor.

(1)** Campo 14 - VL\_SLD\_CREDOR\_TRANSPORTAR:**

Resultado da equação:

(soma dos campos 2 ate 5) - (soma dos campos 6 até 10 mais 12)

Se o valor for maior que “0” (zero), este campo deve ser preenchido com “0” (zero). Se for menor que “0” (zero), o valor absoluto do resultado deve ser informado neste campo.

(1)** Campo 15 - DEB\_ESP:**

Os ajustes lançados na tela Ajuste da Apuração de ICMS e ICMS ST com o campo Tipo apuração igual a **'Débito Especial'** ou com o campo **'Débitos especiais'** marcado, serão totalizados nesse campo do registro.
