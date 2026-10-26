---
id: "25948513490967"
titulo: "EFD FISCAL - ICMS/IPI: campo 20 VL_OUT_DA do registro C100"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/25948513490967-EFD-FISCAL-ICMS-IPI-campo-20-VL-OUT-DA-do-registro-C100"
trilha: "Dúvidas Frequentes > Fiscal e Contábil"
atualizado_em: "2026-07-22T14:43:48Z"
rotulos: ["Configuração", "IPI", "ICMS", "Impostos", "TOP", "EFD"]
---

# EFD FISCAL - ICMS/IPI: campo 20 VL_OUT_DA do registro C100

**(1)** Confira abaixo orientações sobre as regras sistêmicas para o cálculo e preenchimento do campo 20 - VL\_OUT\_DA do registro C100.

Se no cadastro da TOP da nota lançada, que está sendo gerada no registro C100, o campo **"Operação sem direito a crédito IPI/ST"** estiver **marcado,** ou, a UF da empresa geradora do txt está no parâmetro **"UFEFDVLMERC"**, esse campo será apenas o valor do campo 'vlr destaque' da nota.

Se no ambiente de configuração nenhuma dessas afirmações acima forem verdadeiras, o sistema analisará o parâmetro UFEFDOUTRAS. Se a UF da empresa geradora do TXT estiver informada e, também no livro fiscal da nota não foi apropriado valor de IPI em campo próprio e na nota **HÁ** valores de IPI na tela **"Consultar/alterar dados dos impostos do item"** (TGFDIN), o sistema vai levar pra o campo citado, o valor do IPI da nota presente na tela Consultar/alterar dados dos impostos do item (TGFDIN).

**Observação:** no parâmetro UFEFDOUTRAS deve ser configurado a UF entre virgulas, exemplo: **,MG,**
