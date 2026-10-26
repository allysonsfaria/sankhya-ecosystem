---
id: "360048634673"
titulo: "Sped Fiscal : Bloco DIFAL e FCP [Registros  E300, E310, E311, E312, E313 e E316]"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360048634673-Sped-Fiscal-Bloco-DIFAL-e-FCP-Registros-E300-E310-E311-E312-E313-e-E316"
trilha: "Dúvidas Frequentes > Fiscal e Contábil"
atualizado_em: "2026-10-16T16:39:41Z"
rotulos: ["Configuração", "DIFAL", "ICMS", "Impostos", "EFD", "Configuração: Insira registros E300 E310 E311 E312 E313 E316 nas Preferências da Empresa.", "Ajuste: Atualize campos DIFAL e FCP na tela de Ajuste de ICMS e na tela de Apuração.", "Geração: Execute a geração do EFD e verifique os registros DIFAL e FCP no validador.", "FCP"]
---

# Sped Fiscal : Bloco DIFAL e FCP [Registros  E300, E310, E311, E312, E313 e E316]

**![Imagem 1: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/19604546794903) SOLUÇÃO:**

A EFD – Escrituração Fiscal Digital, mais conhecida como Sped Fiscal, recebeu no bloco E novos registros referentes às operações interestaduais destinadas a consumidores finais não contribuinte do ICMS, onde tem incidência do cálculo do Difal (Diferencial de Alíquota) e FCP (Fundo de Combate à Pobreza).

Para obtermos estes novos registros no Sped Fiscal, o usuário deve se atentar às seguintes configurações:

![Imagem 2: Insira nas Preferências da Empresa (Comercial » Preferências » Empresa) , aba ‘EFD – Escrituração Fiscal Digital’, Tipo…](https://ajuda.sankhya.com.br/hc/article_attachments/20471203396119) Insira nas Preferências da Empresa (Comercial » Preferências » Empresa), aba ‘EFD – Escrituração Fiscal Digital’, Tipo de Escrituração = EFD, posicionar no bloco E, e inserir o registros:

- E300, E310, E311, E312, E313 e E316;

![Imagem 3: E300, E310, E311, E312, E313 e E316;](https://ajuda.sankhya.com.br/hc/article_attachments/19604554677015)

![Imagem 4: Insira nas Preferências da Empresa, aba ‘EFD – Escrituração Fiscal Digital’ ( Comercial » Preferências » Empresa) ,…](https://ajuda.sankhya.com.br/hc/article_attachments/19604554681751) Insira nas Preferências da Empresa, aba ‘EFD – Escrituração Fiscal Digital’ (Comercial » Preferências » Empresa), Tipo de Escrituração = EFD, posicionar no bloco C e depois no bloco D, e inserir o registros

- C101 e D101;

![Imagem 5: Execute a Geração ICMS/IPI – Livros Fiscais;](https://ajuda.sankhya.com.br/hc/article_attachments/19604546807063) Execute a Geração ICMS/IPI – Livros Fiscais;

![Imagem 6: Verifique se foram geradas os campos do DIFAL e FCP na tela ‘Cadastro ICMS/IPI’, aba ICMS/IPI, coluna do ICMS, campos…](https://ajuda.sankhya.com.br/hc/article_attachments/19604554688919) Verifique se foram geradas os campos do DIFAL e FCP na tela ‘Cadastro ICMS/IPI’, aba ICMS/IPI, coluna do ICMS, campos novos:

- ‘Valor DIFAL UF Remet’;
- ‘Valor DIFAL UF Destino’;
- ‘Vlr.Fun.Comb.Pobreza’;

![Imagem 7: Os ajustes serão feitos na tela ‘Ajuste da Apuração de ICMS e ICMS ST’ (Livros Fiscais » Arquivos) :](https://ajuda.sankhya.com.br/hc/article_attachments/19604546810263) Os ajustes serão feitos na tela ‘Ajuste da Apuração de ICMS e ICMS ST’ (Livros Fiscais » Arquivos):

- O campo **‘Tipo de Ajuste’** está aberto para inserir texto livro, porém, se o usuário não preenche-lo, o mesmo irá ser gravado com a expressão ‘9999’, a qual compõe o código de ajuste do registro E311;
- No campo ‘**Tipo Imposto’**, inserimos os dois novos tipos: **ICMS DIFAL** e **ICMS FCP**;
- O campo **‘Cód.UF’** deverá ser preenchido pela UF do ajuste do DIFAL ou FCP;

Foram criados novos filtros na sub-tela ‘Pesquisa de Notas para Detalhes do Ajuste’ – Filtros para DIFAL e FCP:

-> ‘UF Destino:’ = deverá ser escolhida a UF de Destino das NFe para ajustes;

-> ‘Opções para o valor de ajuste:’ = Neste campo há três escolhas para o usuário escolher, para que venha os valores já informados no campo ‘Vlr.Ajuste”:

![Imagem 8: -> ‘Opções para o valor de ajuste:’ = Neste campo há três escolhas para o usuário escolher, para que venha os valores…](https://ajuda.sankhya.com.br/hc/article_attachments/19604546816663)

- Valor Zero – default = 0,00. O usuário irá digitar o valor do ajuste;
- Valor DIFAL UF Remetente – default = Valor do DIFAL, parcela do Remetente. O usuário poderá alterar o valor;
- Valor DIFAL/FCP UF Destino – default = Valor do DIFAL e FCP, parcela do Destinatário. O usuário poderá alterar o valor;

![Imagem 9: Na tela “Obrigações do ICMS e ICMS ST a Recolher” foi inserido, no campo “Tipo de Apuração”, os tipos ICMS DIFAL e ICMS…](https://ajuda.sankhya.com.br/hc/article_attachments/19604546820759) Na tela “Obrigações do ICMS e ICMS ST a Recolher” foi inserido, no campo “Tipo de Apuração”, os tipos ICMS DIFAL e ICMS FCP;

![Imagem 10: Para geração do EFD (Sped Fiscal), se faz necessário gerar o 'Registro de Apuração do ICMS' (Livros Fiscais »…](https://ajuda.sankhya.com.br/hc/article_attachments/19604554696983) Para geração do EFD (Sped Fiscal), se faz necessário gerar o 'Registro de Apuração do ICMS' (Livros Fiscais » Relatórios), tendo que informar Empresa, Período e fazer a seguinte execução:

- **Abrir -> Visualizar -> Salvar** – Neste momento o usuário somente verá as informações do ICMS Próprio, porém, ao executar esta tarefa, está gerando os registros de DIFAL e FCP nas tabelas de Apuração, porém, ainda não há relatório para o mesmo.

![Imagem 11: Após executar o Apuração do ICMS, gerar o EFD (Sped Fiscal) em Conexão -> EFD – Escrituração Fiscal Digital. Neste…](https://ajuda.sankhya.com.br/hc/article_attachments/19604546827287) Após executar o Apuração do ICMS, gerar o EFD (Sped Fiscal) em Conexão -> EFD – Escrituração Fiscal Digital. Neste deverão ter os registros do DIFAL e FCP: E300, E310, E311, E312, E313 e E316. Ao importar o arquivo para o validador, o mesmo irá demonstrar o apuração do DIFAL/FCP feito por UF, conforme tela abaixo:

![Imagem 12: Após executar o Apuração do ICMS, gerar o EFD (Sped Fiscal) em Conexão -> EFD – Escrituração Fiscal Digital. Neste…](https://ajuda.sankhya.com.br/hc/article_attachments/19604546831127)
