## DBLP Dataset

### Description
数据集描述和PPT制作请参考`description`文件夹。

### Usage
#### 方式一：下载现成csv数据

数据已经预处理转换为了csv格式数据，直接下载`dataset`文件夹中dblp-2024-10-01.zip，解压获得csv格式数据集，进行后续使用。

链接：https://pan.baidu.com/s/1ryYt0v-RF7fX1E_gGRMUNA?pwd=3riv 
提取码：3riv

#### 方式二：自行下载处理xml数据
1. 从[DBLP](https://dblp.uni-trier.de/xml)上下载数据集。建议使用[`release/`](https://dblp.org/xml/release/)中的10月份稳定版本: `dblp-2024-10-01.xml.gz`，解压后得到`dblp-2024-10-01.xml`。
2. 从[DBLP](https://dblp.uni-trier.de/xml)上下载数据集的DTD文件，文件名为`dblp.dtd`。
3. 处理xml数据，得到csv数据：
    ```
    pip install dblp-sax-parser
    python process.py
    ```
    dblp-sax-parser使用参考：[dblp-sax-parser](https://pypi.org/project/dblp-sax-parser/)