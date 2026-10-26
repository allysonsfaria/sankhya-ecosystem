---
id: "5914905612567"
titulo: "Veja como é gerado I052 na ECD"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/5914905612567-Veja-como-%C3%A9-gerado-I052-na-ECD"
trilha: "Melhores Práticas > Fiscal e Contábil"
atualizado_em: "2026-07-22T15:17:32Z"
rotulos: ["Configuração", "ECD", "Contabilidade", "#validadoThiagoArantes", "Códigos de aglutinação no I052 estão vinculados aos demonstrativos contábeis do bloco J.", "O código aglutinador é o código da estrutura do Balanço e DRE.", "Na tela \"Empresa\" marque o registro para gerar o I052.", "Documentos Eletrônicos", "Registro I052"]
---

# Veja como é gerado I052 na ECD

#### Registro I052: Indicação dos Códigos de Aglutinação

No sistema os códigos aglutinadores do registro I052 estão relacionados às configurações dos demonstrativos contábeis que iremos tratar no bloco J.

Quando falamos de código de aglutinação estamos falando do código das estruturas do J100 e J150 quanto as contas vinculadas na estrutura de cada um. O código que vai gerar no I052 é o código da estrutura do Balanço e da DRE.

**Veja o exemplo.**

Tem-se na estrutura da DRE, no código de aglutinação **1.1 -RECEITA BRUTA** vinculado a conta **3.1.1.10.0001 - VENDA DE MERCADORIAS A VISTA**, logo no I052 será gerado o código de aglutinação **1.1 -RECEITA BRUTA** .

![Imagem 1: Tem-se na estrutura da DRE, no código de aglutinação 1.1 -RECEITA BRUTA vinculado a conta 3.1.1.10.0001 - VENDA DE…](https://ajuda.sankhya.com.br/hc/article_attachments/15776951742743)

Veja como Gerou no ttxt

|I050|01012010|04|A|5|3.1.1.10.001|3.1.1.10 |VENDA DE MERCADORIAS A VISTA|

|I051|0|3.11.01.05.01.26|

|I052||1.1|

Ou seja, toda conta contábil vinculada a uma linha analítica da estrutura da DRE ou do Balanço, quando gerar o I050 vai gerar o código aglutinador no I052.

**![Imagem 2: Importante:](https://ajuda.sankhya.com.br/hc/article_attachments/16426896776855) Importante:**

Não esqueça que na tela **"Empresa"** (Caminho de acesso: contabilidade> Preferências), aba **"ECD"** cadastre e marque o  Registro para gerar.

![Imagem 3: Não esqueça que na tela "Empresa" (Caminho de acesso: contabilidade> Preferências), aba "ECD" cadastre e marque o…](https://ajuda.sankhya.com.br/hc/article_attachments/15776966956823)
