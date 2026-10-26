---
id: "43547162929687"
titulo: "Erro de chave primária ao processar EFD Fiscal: PK_TGFEFDF0190 - Violação da restrição PRIMARY KEY 'PK_TGFEFDF0190'. Não é possivel inserir a chave duplicada no objeto 'JNA. TGFEFDF0190'. O valor de chave duplicada é (1, Jan 1 2025 12:00AM, 0001, PEÇ)."
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/43547162929687-Erro-de-chave-prim%C3%A1ria-ao-processar-EFD-Fiscal-PK-TGFEFDF0190-Viola%C3%A7%C3%A3o-da-restri%C3%A7%C3%A3o-PRIMARY-KEY-PK-TGFEFDF0190-N%C3%A3o-%C3%A9-possivel-inserir-a-chave-duplicada-no-objeto-JNA-TGFEFDF0190-O-valor-de-chave-duplicada-%C3%A9-1-Jan-1-2025-12-00AM-0001-PE%C3%87"
trilha: "Solução de Problemas > Fiscal e Contábil "
atualizado_em: "2026-10-09T12:40:19Z"
rotulos: ["Artigo criado KCS", "Fiscal/Contábil - KCS"]
---

# Erro de chave primária ao processar EFD Fiscal: PK_TGFEFDF0190 - Violação da restrição PRIMARY KEY 'PK_TGFEFDF0190'. Não é possivel inserir a chave duplicada no objeto 'JNA. TGFEFDF0190'. O valor de chave duplicada é (1, Jan 1 2025 12:00AM, 0001, PEÇ).

**MENSAGEM**

Violação da restrição PRIMARY KEY 'PK\_TGFEFDF0190'. Não é possível inserir a chave duplicada no objeto 'JNA. TGFEFDF0190'. O valor de chave duplicada é (1, Jan 1 2025 12:00AM, 0001, PEC).

**SITUAÇÃO**

Ao gerar o SPED Fiscal (EFD ICMS/IPI), o processamento para com a mensagem acima quando o sistema grava o registro 0190 (Identificação das unidades de medida) na tabela TGFEFDF0190.

O erro ocorre em bancos SQL Server quando a mesma unidade de medida está gravada em mais de uma forma, com e sem acento (por exemplo, PEÇ e PEC), em produtos ou em itens de notas do período.

**SOLUÇÃO**

Para solucionar o erro de chave primária duplicada na tabela **"TGFEFDF0190"**, siga o passo a passo abaixo:

**(1)** **Identifique a unidade em conflito.**
Ela é o último valor da chave na mensagem de erro. No exemplo, (1, Jan 1 2025 12:00AM, 0001, PEÇ) indica a empresa 1, o período 01/2025 e a unidade PEÇ.

**(2)** **Confira a grafia da unidade na tela Unidades.**
Pesquise pela unidade informada no erro e observe como ela está escrita, com ou sem acento. Essa é a forma correta, e as demais devem ser ajustadas para ela. No exemplo, considere que a unidade cadastrada é PEC.

**(3)** **Corrija os cadastros dos produtos.**
Na tela Produtos, localize os produtos que usam essa unidade e compare a grafia com a da tela Unidades. Onde estiver diferente (por exemplo, PEÇ em vez de PEC), altere para a forma cadastrada. Verifique também:

- as unidades alternativas dos produtos;
- o relacionamento Parceiro x Produto, se a empresa trabalha com unidade do parceiro.

**(4)** **Corrija as notas já lançadas, se necessário.**
Se o erro continuar depois dos ajustes nos cadastros, há notas do período lançadas com a grafia divergente. Essas notas são corrigidas direto no banco de dados. A correção deve ser feita pelo TI da empresa, com backup prévio. Se a empresa não tiver TI ou o volume for alto, acione o Time de Unidade.

**(5)** **Gere o EFD Fiscal novamente.**

- Se o erro voltar com outra unidade, repita os passos para ela.
- Se voltar com a mesma unidade depois das correções, a forma divergente pode estar em outra origem usada pelo registro 0190, como cupom fiscal ou inventário (Bloco H). Nesse caso, acione o suporte.

**CAUSA**

O registro 0190 lista cada unidade de medida usada no arquivo, vinda de produtos, itens de notas, unidades alternativas, unidades do parceiro, inventário e outras origens. Ao montar essa lista, o sistema ignora diferenças de maiúsculas e minúsculas, mas considera acentos. Por isso PEÇ e PEC entram como duas unidades diferentes.

Já o SQL Server, quando configurado para desconsiderar acentos, trata PEÇ e PEC como o mesmo valor. A unidade faz parte da chave primária da TGFEFDF0190, então a segunda gravação é recusada por chave duplicada.

A divergência costuma passar despercebida no dia a dia porque, para o banco, as duas formas são a mesma unidade. Diferenças apenas de maiúsculas e minúsculas (por exemplo, pc e PC) não causam esse erro.
