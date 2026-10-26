---
id: "360045094493"
titulo: "Melhores práticas - Configuração e geração dos registros C110,C112 e C113 no SPED ICMS/IPI"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360045094493-Melhores-pr%C3%A1ticas-Configura%C3%A7%C3%A3o-e-gera%C3%A7%C3%A3o-dos-registros-C110-C112-e-C113-no-SPED-ICMS-IPI"
trilha: "Melhores Práticas > Fiscal e Contábil"
atualizado_em: "2026-07-22T15:51:11Z"
rotulos: ["1181455", "Configuração", "NF-e", "IPI", "ICMS", "EFD", "Financeiro", "Dados complementares da nota fiscal", "Documento de arrecadação referenciado", "Documentos fiscais referenciados", "Artigo atualizado KCS", "Fiscal/Contábil - KCS", "Documentos Eletrônicos"]
---

# Melhores práticas - Configuração e geração dos registros C110,C112 e C113 no SPED ICMS/IPI

**REGISTRO C110: INFORMAÇÃO COMPLEMENTAR DA NOTA FISCAL (CÓDIGO 01, 1B, 04 E 55)**

Os registros C110 (Informações Complementares da Nota Fiscal) e C113 (Documento Fiscal Referenciado) são essenciais para a correta escrituração fiscal no SPED ICMS/IPI.

HIERARQUIA DOS REGISTROS (layout SPED):
- O C110 é filho do C100.
- O C113 (assim como C111, C112, C114, C115 e C116) é filho do C110.
- O registro 0450 pertence ao Bloco 0 e NÃO é "pai" do C110. O C110 apenas o referencia por meio do campo "02 COD\_INF".

Portanto, para gerar o C113 é necessário que exista o C110 correspondente; e o C110, por sua vez, é gerado dentro do C100.

IMPORTANTE SOBRE O REGISTRO 0450:
No sistema, o conteúdo do 0450 é montado automaticamente a partir da geração do C110 — cada observação utilizada no C110 alimenta o 0450. Por isso, para que o 0450 seja efetivamente escrito no arquivo, basta que ele esteja marcado na configuração de Blocos e Registros. Não é necessário (nem possível) "gerar o 0450 antes do C110": a relação é a inversa, o 0450 é derivado do C110.

Este registro tem por objetivo identificar os dados contidos no campo Informações Complementares da Nota Fiscal que sejam de interesse do fisco. Devem ser discriminadas em registros "filhos próprios" as informações relacionadas com documentos fiscais, processos, cupons fiscais, documentos de arrecadação e locais de entrega ou coleta que foram explicitamente citadas no campo "Informações Complementares" da Nota Fiscal.

OBSERVAÇÃO IMPORTANTE: Mesmo com a opção "Gerar registros C110/.../C115" marcada, o registro C110 NÃO é gerado para NFC-e (modelo 65). A opção libera o C110 apenas para NF-e (modelo 55) de emissão própria; para o modelo 65 existe uma condição independente que bloqueia a geração do C110 de qualquer forma. (Comportamento a confirmar com o desenvolvimento — ver item 3 dos ajustes ao final.)

**(1)"Preferências"** (Comercial >> Cadastros >> Preferências >> Empresa)

Aba: EFD - Escrituração Fiscal Digital

Tipo de Escrituração: EFD
Aba: Blocos e Registros: Marque o Bloco C para gerar.
Guia registros: Marque o C100 e C110 para gerar na entrada e na saída.

Marque também o registro 0450.

Como o registro é para listar as informações complementares dos documentos fiscais, é necessário que tais documentos tenham uma observação padrão informada, então prossiga ao cadastro da observação:

**(2)"Observações para Notas"** (Comercial >> Arquivo >> Cadastros >> Observações para Notas)

Geração no EFD: = [Informações Complementares do Documento Fiscal]

Caso necessite que o conteúdo do campo **"03-TXT\_COMPL"** do registro C110 seja preenchido, marque a opção **"Carrega Complemento p/ EFD"**. Observação: o conteúdo do TXT\_COMPL é limitado a 255 caracteres.

Dica: se o fisco exigir uma codificação específica no campo "COD\_INF" do 0450/C110, informe-a no campo "Cód. Ref. Inf. Complementar" da observação. Quando preenchido, esse código substitui o código padrão no COD\_INF.

**(3)"Portal de Vendas"** (Comercial >> Consulta >> Portal de Vendas)

Após configurada a observação padrão, vincule essa observação à nota fiscal, cujo modelo esteja entre os especificados na descrição do registro.

**(4)"Geração ICMS/IPI"** (Livros Fiscais >> Arquivos >> Geração ICMS/IPI)

Após confirmação da NFe, a próxima etapa é a geração das mesmas nos livros fiscais.

**(5)"EFD - Escrituração Fiscal Digital - ICMS/IPI"** (Livros Fiscais >> Conexão >> EFD - Escrituração Fiscal Digital - ICMS/IPI)

Preencha os filtros conforme necessário (Empresa, período que englobe as notas) e gere o arquivo.

**Observações sobre a geração:**

- Se for uma nota de emissão própria, marque a opção "Gerar registros C110/C111/C112/C113/C114/C115" na aba "Opções" da tela de geração do EFD ICMS/IPI. Sem essa opção, os registros não são gerados para documentos de emissão própria dos modelos 55 e 65. Atenção: especificamente o C110 não é gerado para NFC-e (modelo 65) mesmo com a opção marcada (ver Observação Importante acima).
- Certifique-se de que não há chaves em duplicidade para a mesma nota de origem.
- Verifique se o registro 0450 está marcado, pois ele lista as observações padrão utilizadas e é referenciado pelo C110.

#### REGISTRO C112: DOCUMENTO DE ARRECADAÇÃO REFERENCIADO

Este registro deve ser apresentado, obrigatoriamente, quando no campo **"Informações Complementares"** da nota fiscal constar a identificação de um documento de arrecadação.

Configurações: Primeiramente, configure a geração dos blocos e registros (C112) seguindo a mesma lógica do C110. Configure uma observação padrão marcada para **"Vincular DAE/GNRE"**.

**(1)"Observações para Notas"** (Comercial >> Arquivo >> Cadastros >> Observações para Notas)
**(2)"Tipos de Título"** (Financeiro >> Arquivos >> Cadastros >> Tipos de Título)
**(3)"Preferências"** (Configurações >> Avançado >> Preferências - Parâmetros: TIPTITDAE e TIPTITGNREST).

Após a associação do financeiro de despesa referente ao GNRE com a nota fiscal (via Financeiro >> Rotinas >> Associar autenticação do DAE e GNRE), gere o EFD ICMS/IPI.

#### REGISTRO C113: DOCUMENTO FISCAL REFERENCIADO

Este registro tem por objetivo informar, detalhadamente, outros documentos fiscais mencionados nas informações complementares (ex: remessa de venda para entrega futura e devolução de compras).

**Configurações:**

**(1)** Habilite o registro C113 na tela **"Configuração de Blocos e Registros"** seguindo a lógica do C110.
**(2)** Acesse a tela **"Tipos de Operação - TOP"** (Comercial >> Arquivo >> Cadastros >> Tipos de Operação - TOP) da nota de origem, na aba **"Validações"**, marque a opção **"Buscar NF de origem p/ referenciar na NFe"**.
**(3)** Certifique-se de que a nota de destino possui ligações com as notas de origem. O sistema verificará nos **"Documentos Relacionados"** as informações para gerar o C113.
**(4)** Para notas complementares, verifique se a **"Chave NFe Referenciada"** está preenchida no cabeçalho da nota.
**(5)** Gere os livros fiscais e o SPED seguindo o mesmo processo descrito para o C110.
**(6)** O registro C113 será gerado apenas quando a nota estiver corretamente vinculada à sua origem.

**Observação:** Quando a NFC-e possuir frete incluso, no registro C100 o campo **"18 VL\_FRT"** será zerado.
