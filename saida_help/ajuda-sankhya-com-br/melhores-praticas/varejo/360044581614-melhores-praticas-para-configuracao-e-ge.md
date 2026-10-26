---
id: "360044581614"
titulo: "Melhores Práticas para Configuração e Geração do Bloco X - Fast Service"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044581614-Melhores-Pr%C3%A1ticas-para-Configura%C3%A7%C3%A3o-e-Gera%C3%A7%C3%A3o-do-Bloco-X-Fast-Service"
trilha: "Melhores Práticas > Varejo"
atualizado_em: "2026-07-22T15:50:53Z"
rotulos: ["#criadoRoger", "#revisadojunior", "Configuração", "ECF", "Fiscal", "Fast Service", "XML", "Estoque", "Registra cupons fiscais e estoque mensal", "Importar certificado digital e instalar aplicativo", "Configure no Fast Service e envie XMLs automaticamente", "Bloco X"]
---

# Melhores Práticas para Configuração e Geração do Bloco X - Fast Service

O Bloco X é um dos registros obrigatórios da Escrituração Contábil Fiscal (ECF). Ele é integrado ao Programa Aplicativo Fiscal (PAF-ECF), que é utilizado para transmitir informações sobre os cupons fiscais emitidos por uma empresa. Entre as informações que o Bloco X permite ao negócio enviar para a Receita Federal, temos:

- Um arquivo com dados sobre o estoque mensal do estabelecimento comercial.
- Um arquivo com informações referentes à Redução Z do PAF-ECF, criado diariamente e enviado em ordem sequencial ascendente.

**Configurando Certificado:**
Para o funcionamento do aplicativo de envio do BlocoX, será necessário a importação do certificado
digital da empresa para o seu navegador.

Após a importação do certificado:

Instalação do aplicativo Bloco X:

**Resumo:** O aplicativo Bloco X é responsável pelo envio das informações da Redução Z e Estoque para o Fisco, ele será executado junto ao Fast Service sempre que houver uma tentativa envio seja ela automática ou manual, siga os passos a baixo para realizar a instalação:

Instale o aplicativo de envio do BlocoX, executando o arquivo “Instalador\_BlocoX\_4\_24.exe”

**Configuração no Fast Service:**
No Fast Service acessar a tela de parâmetros:

Na tela de parâmetros na aba Miscelânea:
Para utilização do BlocoX os seguintes parâmetros deverão estar preenchidos:

Após a instalação e configuração realizada com sucesso, O Fast Service estará pronto para utilização
do bloco X.

**Envio das informações ao FISCO:**

O envio das informações da redução Z e estoque é realizado automaticamente através do aplicativo
Bloco X em forma de XML, ao entrar no Fast Service com usuário Caixa.

Caso ocorra algum problema no envio ou o usuário tenha vários documentos pendentes e queira
enviar um documento específico o envio pode ser realizado pelas opções do ‘Menu Fiscal’:

Ao selecionar uma das opções acima será aberto a seguinte tela onde é exibido todos documento
enviados e pendentes :

**Observação**: OS arquivos XML referente a Redução Z e Estoque ficam armazenados nas tabelas
TGFRZF e TGFESF respectivamente
