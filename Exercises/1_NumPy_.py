{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Day 2-3 NumPy .ipynb",
      "provenance": [],
      "collapsed_sections": [
        "JTrU1wvuWkKM",
        "2ECzhrtNg_Ik",
        "7Sn6aLfwkflL",
        "9hujUIlEmS1I",
        "LMk-s144nvdI",
        "I398wU2Tqy60",
        "dQbhDRKhsj4o",
        "mo5c1aujtp6c",
        "YGwxLdKMtvAO",
        "xjYPVo4Ut4k6",
        "sjIzfV9UN9NN",
        "PbzBhobdQKSq",
        "jrfncdIRWDvc",
        "5uZOLUj9XFQR",
        "sqhiESkzYjnu"
      ],
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/aubrin-s/AEOP-REAP/blob/master/Exercises/1_NumPy_.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "ehI7mvOSWNbx",
        "colab_type": "text"
      },
      "source": [
        "NumPy Exercises "
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "JTrU1wvuWkKM",
        "colab_type": "text"
      },
      "source": [
        "# TASK 1 [Arrays]"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "msShw3jHqFet",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 129
        },
        "outputId": "c836bb0a-ee00-4882-faa5-808335ec977d"
      },
      "source": [
        "import numpy\n",
        "\n",
        "print numpy.array(raw_input().split(),float)[::-1]"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "error",
          "ename": "SyntaxError",
          "evalue": "ignored",
          "traceback": [
            "\u001b[0;36m  File \u001b[0;32m\"<ipython-input-33-c5d1ecb9f4ba>\"\u001b[0;36m, line \u001b[0;32m3\u001b[0m\n\u001b[0;31m    print numpy.array(raw_input().split(),float)[::-1]\u001b[0m\n\u001b[0m              ^\u001b[0m\n\u001b[0;31mSyntaxError\u001b[0m\u001b[0;31m:\u001b[0m invalid syntax\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "K04kKY3WXMYp",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 129
        },
        "outputId": "df4edad6-80f4-489c-cf04-8ebf0a9ce7ae"
      },
      "source": [
        "import numpy\n",
        "\n",
        "def arrays(arr):\n",
        "    # complete this function\n",
        "    # use numpy.array\n",
        "\n",
        "arr = raw_input().strip().split(' ')"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "error",
          "ename": "IndentationError",
          "evalue": "ignored",
          "traceback": [
            "\u001b[0;36m  File \u001b[0;32m\"<ipython-input-4-2322f24d75f7>\"\u001b[0;36m, line \u001b[0;32m7\u001b[0m\n\u001b[0;31m    arr = raw_input().strip().split(' ')\u001b[0m\n\u001b[0m      ^\u001b[0m\n\u001b[0;31mIndentationError\u001b[0m\u001b[0;31m:\u001b[0m expected an indented block\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "bLJL-KIXZhkE",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 34
        },
        "outputId": "bac6e628-3992-4084-c516-9f2e99e9f5bb"
      },
      "source": [
        "import numpy\n",
        "A = [1, 2, 3, 4, -8, -10]\n",
        "\n",
        "def arrays(arr):\n",
        "  arr = raw_input().strip().split(' ')\n",
        "A.reverse()\n",
        "print(A)"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "[-10, -8, 4, 3, 2, 1]\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "IyX514j8crJB",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 34
        },
        "outputId": "93782575-53b6-4b53-bad8-62b7e24f5f5e"
      },
      "source": [
        "import numpy as np\n",
        "A = [1, 2, 3, 4, -8, -10]\n",
        "\n",
        "ArrayA= np.array(A, dtype=np.float32)\n",
        "\n",
        "\n",
        "print(ArrayA)"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "[  1.   2.   3.   4.  -8. -10.]\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "2ECzhrtNg_Ik",
        "colab_type": "text"
      },
      "source": [
        "# TASK 2 [Shape and Rephape] Complete\n"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "t9g_OCN3hIFR",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 34
        },
        "outputId": "8350659a-ad94-4c48-c7d8-d9c87b35d039"
      },
      "source": [
        "import numpy\n",
        "\n",
        "my_1D_array = numpy.array([1, 2, 3, 4, 5])\n",
        "print(my_1D_array.shape)"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "(5,)\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "KxD5nIGyjcCE",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 68
        },
        "outputId": "0a717db0-42ba-4b2f-93d8-28ed3ee90fd9"
      },
      "source": [
        "import numpy\n",
        "\n",
        "change_array = numpy.array([1,2,3,4,5,6,7,8,9])\n",
        "change_array.shape = (3, 3)\n",
        "print(change_array)     "
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "[[1 2 3]\n",
            " [4 5 6]\n",
            " [7 8 9]]\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "7Sn6aLfwkflL",
        "colab_type": "text"
      },
      "source": [
        "# TASK 3 [Transpose and Flatten] Complete"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "NAUP5pW8kmYv",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 68
        },
        "outputId": "5d1047e0-ae69-4722-e9a5-d126e277081c"
      },
      "source": [
        "import numpy\n",
        "\n",
        "my_array = numpy.array([[1,2],\n",
        "                        [3,4]])\n",
        "print(numpy.transpose(my_array))\n",
        "\n",
        "my_array = numpy.array([[1,2],\n",
        "                        [3,4]])\n",
        "print(my_array.flatten())\n"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "[[1 3]\n",
            " [2 4]]\n",
            "[1 2 3 4]\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "9hujUIlEmS1I",
        "colab_type": "text"
      },
      "source": [
        "# TASK 4 [Concatenate]"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "TWUzZc1gnO_E",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 231
        },
        "outputId": "6e529331-b21d-4966-ef8e-c4f552753a5a"
      },
      "source": [
        "import numpy\n",
        "\n",
        "array_1 = numpy.array([[1,2,3],[0,0,0]])\n",
        "array_2 = numpy.array([[0,0,0],[7,8,9]])\n",
        "\n",
        "print(numpy.concatenate(array_1, array_2), axis = 1)"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "error",
          "ename": "TypeError",
          "evalue": "ignored",
          "traceback": [
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
            "\u001b[0;31mTypeError\u001b[0m                                 Traceback (most recent call last)",
            "\u001b[0;32m<ipython-input-29-222de61ee3a0>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m()\u001b[0m\n\u001b[1;32m      4\u001b[0m \u001b[0marray_2\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mnumpy\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0marray\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;36m0\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;36m0\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;36m0\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;36m7\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;36m8\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;36m9\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      5\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m----> 6\u001b[0;31m \u001b[0mprint\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mnumpy\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mconcatenate\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0marray_1\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0marray_2\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0maxis\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0;36m1\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m",
            "\u001b[0;32m<__array_function__ internals>\u001b[0m in \u001b[0;36mconcatenate\u001b[0;34m(*args, **kwargs)\u001b[0m\n",
            "\u001b[0;31mTypeError\u001b[0m: only integer scalar arrays can be converted to a scalar index"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "LMk-s144nvdI",
        "colab_type": "text"
      },
      "source": [
        "# TASK 5 [Zeros and Ones] looked at answers "
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "cge25P3holA1",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 129
        },
        "outputId": "6f85df75-9a64-4795-d2ca-6959cb8025d7"
      },
      "source": [
        "import numpy\n",
        "N = map(int, raw_input().split())\n",
        "print(numpy.zeros(N, dtype = numpy.int))\n",
        "print numpy.ones(N, dtype = numpy.int)"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "error",
          "ename": "SyntaxError",
          "evalue": "ignored",
          "traceback": [
            "\u001b[0;36m  File \u001b[0;32m\"<ipython-input-32-86386dd933cd>\"\u001b[0;36m, line \u001b[0;32m4\u001b[0m\n\u001b[0;31m    print numpy.ones(N, dtype = numpy.int)\u001b[0m\n\u001b[0m              ^\u001b[0m\n\u001b[0;31mSyntaxError\u001b[0m\u001b[0;31m:\u001b[0m invalid syntax\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "I398wU2Tqy60",
        "colab_type": "text"
      },
      "source": [
        "# TASK 6 [Eye and Identity] Complete"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "szuxYBVmr2rG",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 68
        },
        "outputId": "a94739b0-95bf-4af0-b2bd-5e09e1346f99"
      },
      "source": [
        "import numpy\n",
        "print(numpy.identity(3))"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "[[1. 0. 0.]\n",
            " [0. 1. 0.]\n",
            " [0. 0. 1.]]\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "dQbhDRKhsj4o",
        "colab_type": "text"
      },
      "source": [
        "# TASK 7 [Array Mathematics] looked at answers "
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "z66tWCsXvPtj",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 170
        },
        "outputId": "4e6e472c-f9d4-4b16-a57d-41c7de871606"
      },
      "source": [
        "import numpy\n",
        "\n",
        "n,m=map(int,input().split())\n",
        "A=numpy.array([list(map(int,input().split())) for i in range(n)])\n",
        "B=numpy.array([list(map(int,input().split())) for i in range(n)])\n",
        "print(A+B,A-B,A*B,A//B,A%B,A**B,sep='\\n')"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "1 4\n",
            "1 2 3 4 \n",
            "5 6 7 8 \n",
            "[[ 6  8 10 12]]\n",
            "[[-4 -4 -4 -4]]\n",
            "[[ 5 12 21 32]]\n",
            "[[0 0 0 0]]\n",
            "[[1 2 3 4]]\n",
            "[[    1    64  2187 65536]]\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "GDvGGC7_vqbf",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 231
        },
        "outputId": "efbc81f2-7d20-4166-c225-b8945bfcf866"
      },
      "source": [
        "import numpy\n",
        "l=map(int,raw_input().split())\n",
        "a=[]\n",
        "b=[]\n",
        "for i in range(l[0]):\n",
        "    a.append(map(int,raw_input().split()))\n",
        "for i in range(l[0]):\n",
        "    b.append(map(int,raw_input().split()))\n",
        "a=numpy.array(a)\n",
        "b=numpy.array(b)\n",
        "print(numpy.add(a, b))\n",
        "print(numpy.subtract(a, b))\n",
        "print(numpy.multiply(a, b))\n",
        "print(numpy.divide(a, b))\n",
        "print(numpy.mod(a, b))\n",
        "print(a**b)"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "error",
          "ename": "NameError",
          "evalue": "ignored",
          "traceback": [
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
            "\u001b[0;31mNameError\u001b[0m                                 Traceback (most recent call last)",
            "\u001b[0;32m<ipython-input-38-8320f8817135>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m()\u001b[0m\n\u001b[1;32m      1\u001b[0m \u001b[0;32mimport\u001b[0m \u001b[0mnumpy\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m----> 2\u001b[0;31m \u001b[0ml\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mmap\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mint\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0mraw_input\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0msplit\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m      3\u001b[0m \u001b[0ma\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      4\u001b[0m \u001b[0mb\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      5\u001b[0m \u001b[0;32mfor\u001b[0m \u001b[0mi\u001b[0m \u001b[0;32min\u001b[0m \u001b[0mrange\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0ml\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;36m0\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;31mNameError\u001b[0m: name 'raw_input' is not defined"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "mo5c1aujtp6c",
        "colab_type": "text"
      },
      "source": [
        "# TASK 8 [Floor, Ceil and Rint] Complete"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "jMnXGH6dwOBL",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 68
        },
        "outputId": "e0f4fd48-9b18-423b-9480-2aadaeba4337"
      },
      "source": [
        "import numpy\n",
        "\n",
        "my_array = numpy.array([1.1, 2.2, 3.3, 4.4, 5.5, 6.6, 7.7, 8.8, 9.9])\n",
        "print(numpy.floor(my_array))\n",
        "my_array = numpy.array([1.1, 2.2, 3.3, 4.4, 5.5, 6.6, 7.7, 8.8, 9.9])\n",
        "print(numpy.ceil(my_array))\n",
        "my_array = numpy.array([1.1, 2.2, 3.3, 4.4, 5.5, 6.6, 7.7, 8.8, 9.9])\n",
        "print(numpy.rint(my_array))"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "[1. 2. 3. 4. 5. 6. 7. 8. 9.]\n",
            "[ 2.  3.  4.  5.  6.  7.  8.  9. 10.]\n",
            "[ 1.  2.  3.  4.  6.  7.  8.  9. 10.]\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "YGwxLdKMtvAO",
        "colab_type": "text"
      },
      "source": [
        "# TASK 9 [Sum and Prod] Complete"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "ih9RllITx95d",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 85
        },
        "outputId": "555e929f-086a-4f0b-c817-24dc1827c6f7"
      },
      "source": [
        "import numpy\n",
        "\n",
        "my_array = numpy.array([ [1, 2], [3, 4] ])\n",
        "\n",
        "print(numpy.prod(my_array, axis = 0))           \n",
        "print(numpy.prod(my_array, axis = 1))            \n",
        "print(numpy.prod(my_array, axis = None))        \n",
        "print(numpy.prod(my_array))                   "
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "[3 8]\n",
            "[ 2 12]\n",
            "24\n",
            "24\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "Za2iblO0z4rE",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 34
        },
        "outputId": "16376ae7-519c-4efe-9fdd-74b9eb5dcf6b"
      },
      "source": [
        "import numpy\n",
        "\n",
        "my_array = numpy.array([ [1, 2], [3, 4] ])\n",
        "     \n",
        "print(numpy.prod(my_array))   "
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "24\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "xjYPVo4Ut4k6",
        "colab_type": "text"
      },
      "source": [
        "# TASK 10 [Min and Max] Complete"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "F15XS8ep1v6P",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 34
        },
        "outputId": "4a6968cf-801a-4d19-d08d-f026d2b4107b"
      },
      "source": [
        "import numpy\n",
        "\n",
        "my_array = numpy.array([[10, 5], \n",
        "                        [3, 7],\n",
        "                        [6, 8],\n",
        "                        [4, 9]])\n",
        "print(numpy.min(my_array))"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "3\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "sjIzfV9UN9NN",
        "colab_type": "text"
      },
      "source": [
        "# TASK 11 [Mean, Var, and Std] Complete"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "hHqkX6dHOg3l",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 68
        },
        "outputId": "33bd4c8e-56c3-4098-d7c9-4a781650385b"
      },
      "source": [
        "import numpy\n",
        "\n",
        "my_array = numpy.array([ [1, 2], [3, 4] ])\n",
        "\n",
        "print(numpy.mean(my_array, axis = 1))\n",
        "print(numpy.var(my_array, axis = 0))\n",
        "print(numpy.std(my_array, axis = None))"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "[1.5 3.5]\n",
            "[1. 1.]\n",
            "1.118033988749895\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "PbzBhobdQKSq",
        "colab_type": "text"
      },
      "source": [
        "# TASK 12 [Dot and Cross] "
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "o2J02NB_Qeli",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "import numpy\n",
        "\n",
        "A = numpy.array([ 1, 2], [3, 4 ])\n",
        "print(A * A)\n"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "7LAdpfcQUY2M",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 54
        },
        "outputId": "3d57a89f-3d79-40d0-a994-fb30ea00bd31"
      },
      "source": [
        "import numpy\n",
        "\n",
        "A = numpy.array([[ 1, 2 ],[3,4]])\n",
        "B = numpy.array([[ 1, 2 ],[3,4]])\n",
        "\n",
        "print(numpy.dot(A, B))\n",
        "#print(numpy.cross(A, B))  "
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "[[ 7 10]\n",
            " [15 22]]\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "akvj3oHmV9lA",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "import numpy     #looked it up\n",
        "N = int(raw_input())\n",
        "A = numpy.array([map(int, raw_input().split())for _ in range(N)])\n",
        "B = numpy.array([map(int, raw_input().split())for _ in range(N)])\n",
        "print numpy.dot(A, B)"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "jrfncdIRWDvc",
        "colab_type": "text"
      },
      "source": [
        "# TASK 13 [Inner and and Outer] Complete"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "qIStmb1dWo0m",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 68
        },
        "outputId": "6f3999bb-06cf-4fa7-ed24-b247e42b8a1c"
      },
      "source": [
        "import numpy\n",
        "\n",
        "A = numpy.array([0, 1])\n",
        "B = numpy.array([2, 3])\n",
        "\n",
        "print(numpy.inner(A, B))\n",
        "print(numpy.outer(A, B))"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "3\n",
            "[[0 0]\n",
            " [2 3]]\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "5uZOLUj9XFQR",
        "colab_type": "text"
      },
      "source": [
        "# TASK 14 [Polynomials] Complete"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "9Yfj8v3pXsBr",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 34
        },
        "outputId": "9466b2e9-3de3-46ff-d2b2-44e4de47cf69"
      },
      "source": [
        "import numpy\n",
        "\n",
        "print(numpy.polyval([1.1, 2, 3], 0))"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "3.0\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "sqhiESkzYjnu",
        "colab_type": "text"
      },
      "source": [
        "# TASK 15 [Linear Algebra] Complete\n",
        "\n"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "vmuNwXoHZCfS",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 34
        },
        "outputId": "265376db-9c24-4783-843e-e6ebb11fefec"
      },
      "source": [
        "import numpy\n",
        "\n",
        "print(numpy.linalg.det([[1.1 , 1.1], [1.1, 1.1]]))"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "0.0\n"
          ],
          "name": "stdout"
        }
      ]
    }
  ]
}