---
id: "360051122833"
titulo: "O que é necessário para um documento ser apresentado no Registro C500 - EFD Contribuições"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360051122833-O-que-%C3%A9-necess%C3%A1rio-para-um-documento-ser-apresentado-no-Registro-C500-EFD-Contribui%C3%A7%C3%B5es"
trilha: "Dúvidas Frequentes > Fiscal e Contábil"
atualizado_em: "2026-07-24T13:11:31Z"
rotulos: ["Configuração", "NF-e", "Impostos", "CFOP", "CST", "avulsa", "EFD Contribuições", "Análises necessárias: Configuração C500 CSTs de crédito CFOPs válidos.", "Validação de modelos: Verifique modelos 6 28 29 66 na TOP", "Documentos no Registro C500: NF-e Energia Elétrica Água Gás.", "Registro C500"]
---

# O que é necessário para um documento ser apresentado no Registro C500 - EFD Contribuições

**Quais documentados são gerados no Registro C500 ?**

| - Nota Fiscal/Conta de Energia Elétrica (Código 06) - Nota Fiscal de Energia Elétrica Eletrônica – NF3e (Código 66) - Nota Fiscal/Conta de fornecimento D’água Canalizada (Código 29) - Nota Fiscal/Consumo Fornecimento de Gás (Código 28) - NF-e (Código 55) –Documentos de Entrada / Aquisição com Crédito |
| --- |

**Quais análises devem ser feitas no sistema para geração do Registro C500 ?**

![Imagem 1: Certifique-se que para a respectiva empresa, na tela 'Empresa' (Comercial » Preferências ), na aba 'EFD - Escrituração…](https://ajuda.sankhya.com.br/hc/article_attachments/15936705421207) Certifique-se que para a respectiva empresa, na tela 'Empresa' (Comercial » Preferências), na aba 'EFD - Escrituração Fiscal Digital' para o Tipo de Escrituração 'EFD Contribuições' o registro C500 está devidamente configurado:

![Imagem 2: Certifique-se que para a respectiva empresa, na tela 'Empresa' (Comercial » Preferências ), na aba 'EFD - Escrituração…](https://ajuda.sankhya.com.br/hc/article_attachments/15936690634647)

![Imagem 3: Os lançamentos das notas deverão ter o cálculo de PIS/COFINS, com CST'S que representem crédito dos respectivos…](https://ajuda.sankhya.com.br/hc/article_attachments/15936761799703) Os lançamentos das notas  deverão ter o cálculo de PIS/COFINS, com CST'S que representem crédito dos respectivos impostos. Essa informação deve ser conferida na 'TGFDIN' (Central de notas > Botão outras opções > Opção "Consultar/alterar dados do imposto do item);

- CST's verificados para geração do registro: 50,51,52,53,54,55,56,60,61,62,63,64,65,66

![Imagem 4: Verificar na grade de itens da 'Central de notas' e na tela "Cadastro do livro de ICMS/IPI" se o CFOP está entre um…](https://ajuda.sankhya.com.br/hc/article_attachments/15936705426199) Verificar na grade de itens da 'Central de notas' e na tela "Cadastro do livro de ICMS/IPI" se o CFOP está entre um desses seguintes: (LIV.CODCFO IN)

- CFOP = 1251,1252,1253,1254,1255,1256,1257,2251,2252,2253,2254,2255,2256,2257;

**![Atenção](https://ajuda.sankhya.com.br/hc/article_attachments/15936761808535) IMPORTANTE:**

O sistema só irá validar os CFOP'S citados se o parâmetro GERNFENERC500 estiver ativo, com ele ativo, o sistema busca as notas modelo 55 com os cfops citados, se o item da nota for do tipo 'consumo' em seu cadastro, no campo 'usado como';

![Imagem 6: Verificar se o modelo do documento está entre os seguintes: 6,28,29,66; ( LIV.CODMODDOC IN )](https://ajuda.sankhya.com.br/hc/article_attachments/15936705428631) Verificar se o modelo do documento está entre os seguintes: 6,28,29,66; [LIV.CODMODDOC IN]

- Aba 'Livro Fiscal' >> Campo 'Modelo do Documento >> Tela 'Tipos de Operação - TOP'

**![Atenção](https://ajuda.sankhya.com.br/hc/article_attachments/15936761815191) IMPORTANTE:**

Não basta apenas alterar na TOP, esse campo é histórico. Caso existam alterações, essas só serão válidas para novos lançamentos.
