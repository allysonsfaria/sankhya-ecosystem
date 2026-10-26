---
id: "13458535385367"
titulo: "Retorno das consultas consChNFe e consNSU, as seguintes regras de uso indevido"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/13458535385367-Retorno-das-consultas-consChNFe-e-consNSU-as-seguintes-regras-de-uso-indevido"
trilha: "Solução de Problemas > Mensagens de validação da SEFAZ"
atualizado_em: "2026-07-22T15:00:09Z"
rotulos: ["Configuração", "Consulta", "NF-e", "XML", "SEFAZ", "Regras de Uso Indevido nas Consultas consChNFe e consNSU", "Erro", "Documentos Eletrônicos"]
---

# Retorno das consultas consChNFe e consNSU, as seguintes regras de uso indevido

**(1)** Uma NT da SEFAZ está impactando fortemente esse processo de download dos arquivos XML, segue:

**04/03/2022 - Atualização das Regras de Uso Indevido do Web Service NFeDistribuicaoDFe - NT 2014.002:**
 
<https://www.nfe.fazenda.gov.br/portal/informe.aspx?ehCTG=false&Informe=0cu/yBLKrCs=>
 
Em resumo a SEFAZ determinou que só podem ser realizadas 20 Consultas por Hora, Por CNPJ e Por certificado.

**(1)** Por essa razão, revise algumas configurações para tentar manter a performance da rotina dentro das exigências da SEFAZ:
 
**![Imagem 1: (1) Por essa razão, revise algumas configurações para tentar manter a performance da rotina dentro das exigências da…](https://ajuda.sankhya.com.br/hc/article_attachments/17083607369239) Tela:** Comercial » Rotinas » Configuração MD-e/DF-e

- Observando a tela abaixo é possível identificar que as configurações estão de acordo:

![Imagem 2: Observando a tela abaixo é possível identificar que as configurações estão de acordo:](https://ajuda.sankhya.com.br/hc/article_attachments/13458549786135)

**![Imagem 3: Tela: Comercial » Preferências » Empresa Marque os campos abaixo apenas para empresas que de fato utilizam o recurso.…](https://ajuda.sankhya.com.br/hc/article_attachments/17083607370775) Tela:** Comercial » Preferências » Empresa
Marque os campos abaixo **apenas** para empresas que de fato **utilizam** o recurso. Ou seja, apenas as empresas que tem movimentações e que precisam que seus arquivos sejam importados e **somente** na base de **produção**.

- Caso possuam bases **Treina e teste, desmarque** as opções abaixo para que não efetue buscas:

![Imagem 4: Caso possuam bases Treina e teste, desmarque as opções abaixo para que não efetue buscas:](https://ajuda.sankhya.com.br/hc/article_attachments/13458110055447)

![Imagem 5: OBSERVAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/17083645728663) **OBSERVAÇÃO:**

É importante ressaltar que a SEFAZ está monitorando essas consultas por **todos** os meios de busca, sendo assim orientamos:
 
- Desative a opção de busca nas bases Treina e Teste;
- Evite realizar consultas direto na SEFAZ, utilizando o certificado;
- Evite realizar a busca Manual na rotina **"Configuração MD-e/DF-e"** nas opções **"Consultar Documentos"** e **"Consulta Direta";**
- Evite utilizar outros aplicativos de busca em paralelo (arquivei, fsist entre outros);
- Se o seu certificado estiver em poder de terceiros, solicite que não utilize-o para consultas.
 
As orientações acima são para evitar que a SEFAZ retorne a rejeição:
 
**656 -Motivo: Rejeição: Consumo Indevido**
 
Essa rejeição causa atrasos nos downloads dos arquivos XML e, caso esteja sendo frequente, é possível até mesmo ter outros problemas como o bloqueio pela própria SEFAZ.
 
Orienta-se também que seja feita a reinicialização do **Servidor**.
Caso tenha algum JOB travado, devido essas rejeições ou as instabilidades da SEFAZ, a reinicialização poderá sanar.
 
Destaca-se abaixo 2 pontos importantes:

- Caso possuam mais de 1 empresa utilizando o mesmo certificado, avalie pois a SEFAZ utiliza como critério CNPJ - Certificado, ou seja, se houver várias buscas utilizando CNPJ iguais ou diferentes porém atribuídos a um mesmo Certificado poderá ser retornado a rejeição;
- Outro ponto é sobre o acesso a esses arquivos. A rotina Configuração MD-e/DF-e foi desenvolvida na intenção de facilitar as buscas desses arquivos de maneira automática. Porém, "A SEFAZ reserva-se o direito de permitir o download do XML pelo destinatário para apenas um percentual da média mensal de suas NF-e"

![Imagem 6: Outro ponto é sobre o acesso a esses arquivos. A rotina Configuração MD-e/DF-e foi desenvolvida na intenção de…](https://ajuda.sankhya.com.br/hc/article_attachments/13458197577623)

Avalie bem a NT para que o cenário seja corrigido e as rejeições não aconteçam.

![Imagem 7: Avalie bem a NT para que o cenário seja corrigido e as rejeições não aconteçam.](https://ajuda.sankhya.com.br/hc/article_attachments/13458199973911)
