from rich.console import Console
from rich.columns import Columns
from rich.table import Column, Table
from rich.panel import Panel

console = Console()

jsonList = {
    "spareroomObjList": [
        {
            "acmcBuilding": "207",
            "acmcBuildingName": "四教",
            "claroom": [
                {
                    "classNumberOfSeats": "25",
                    "classroom": "留学中心210",
                    "szlc": ""
                },
                {
                    "classNumberOfSeats": "25",
                    "classroom": "留学中心203",
                    "szlc": ""
                }
            ]
        },
        {
            "acmcBuilding": "201",
            "acmcBuildingName": "临医楼",
            "claroom": [
                {
                    "classNumberOfSeats": "100",
                    "classroom": "五楼实验室",
                    "szlc": ""
                },
                {
                    "classNumberOfSeats": "60",
                    "classroom": "三住15F示教室",
                    "szlc": ""
                },
                {
                    "classNumberOfSeats": "200",
                    "classroom": "临床技能中心",
                    "szlc": ""
                },
                {
                    "classNumberOfSeats": "505",
                    "classroom": "病房",
                    "szlc": ""
                },
                {
                    "classNumberOfSeats": "100",
                    "classroom": "PBL",
                    "szlc": ""
                },
                {
                    "classNumberOfSeats": "98",
                    "classroom": "312",
                    "szlc": ""
                },
                {
                    "classNumberOfSeats": "121",
                    "classroom": "309",
                    "szlc": ""
                },
                {
                    "classNumberOfSeats": "130",
                    "classroom": "305",
                    "szlc": ""
                },
                {
                    "classNumberOfSeats": "100",
                    "classroom": "302",
                    "szlc": ""
                },
                {
                    "classNumberOfSeats": "225",
                    "classroom": "301",
                    "szlc": ""
                },
                {
                    "classNumberOfSeats": "50",
                    "classroom": "226",
                    "szlc": ""
                },
                {
                    "classNumberOfSeats": "60",
                    "classroom": "224",
                    "szlc": ""
                },
                {
                    "classNumberOfSeats": "50",
                    "classroom": "215",
                    "szlc": ""
                },
                {
                    "classNumberOfSeats": "100",
                    "classroom": "214",
                    "szlc": ""
                },
                {
                    "classNumberOfSeats": "60",
                    "classroom": "213",
                    "szlc": ""
                },
                {
                    "classNumberOfSeats": "52",
                    "classroom": "210",
                    "szlc": ""
                },
                {
                    "classNumberOfSeats": "125",
                    "classroom": "209",
                    "szlc": ""
                },
                {
                    "classNumberOfSeats": "125",
                    "classroom": "205",
                    "szlc": ""
                },
                {
                    "classNumberOfSeats": "100",
                    "classroom": "202",
                    "szlc": ""
                },
                {
                    "classNumberOfSeats": "225",
                    "classroom": "201",
                    "szlc": ""
                },
                {
                    "classNumberOfSeats": "67",
                    "classroom": "10-10",
                    "szlc": ""
                }
            ]
        },
        {
            "acmcBuilding": "212",
            "acmcBuildingName": "华西",
            "claroom": [
                {
                    "classNumberOfSeats": "60",
                    "classroom": "一教解剖室105",
                    "szlc": ""
                },
                {
                    "classNumberOfSeats": "60",
                    "classroom": "一教解剖室104",
                    "szlc": ""
                },
                {
                    "classNumberOfSeats": "60",
                    "classroom": "一教解剖室103",
                    "szlc": ""
                },
                {
                    "classNumberOfSeats": "60",
                    "classroom": "一教解剖室102",
                    "szlc": ""
                },
                {
                    "classNumberOfSeats": "60",
                    "classroom": "一教解剖室101",
                    "szlc": ""
                },
                {
                    "classNumberOfSeats": "60",
                    "classroom": "一教解剖室",
                    "szlc": ""
                },
                {
                    "classNumberOfSeats": "120",
                    "classroom": "图书馆四楼东",
                    "szlc": ""
                },
                {
                    "classNumberOfSeats": "40",
                    "classroom": "三教专业实验室203",
                    "szlc": ""
                },
                {
                    "classNumberOfSeats": "40",
                    "classroom": "三教专业实验室202",
                    "szlc": ""
                },
                {
                    "classNumberOfSeats": "60",
                    "classroom": "三教专业实验室231",
                    "szlc": ""
                },
                {
                    "classNumberOfSeats": "500",
                    "classroom": "见习",
                    "szlc": ""
                },
                {
                    "classNumberOfSeats": "99",
                    "classroom": "基1-南",
                    "szlc": ""
                },
                {
                    "classNumberOfSeats": "98",
                    "classroom": "基1-北",
                    "szlc": ""
                },
                {
                    "classNumberOfSeats": "80",
                    "classroom": "荷花池声乐室",
                    "szlc": ""
                },
                {
                    "classNumberOfSeats": "150",
                    "classroom": "妇产科教室",
                    "szlc": ""
                },
                {
                    "classNumberOfSeats": "50",
                    "classroom": "法医三楼实验1",
                    "szlc": ""
                },
                {
                    "classNumberOfSeats": "30",
                    "classroom": "法医三楼VR",
                    "szlc": ""
                },
                {
                    "classNumberOfSeats": "60",
                    "classroom": "法医三楼实验室",
                    "szlc": ""
                },
                {
                    "classNumberOfSeats": "60",
                    "classroom": "法医楼301",
                    "szlc": ""
                },
                {
                    "classNumberOfSeats": "80",
                    "classroom": "法医八楼",
                    "szlc": ""
                },
                {
                    "classNumberOfSeats": "150",
                    "classroom": "儿科教室",
                    "szlc": ""
                }
            ]
        },
        {
            "acmcBuilding": "211",
            "acmcBuildingName": "实验室",
            "claroom": [
                {
                    "classNumberOfSeats": "300",
                    "classroom": "逸夫楼五楼",
                    "szlc": ""
                },
                {
                    "classNumberOfSeats": "200",
                    "classroom": "逸夫楼530",
                    "szlc": ""
                },
                {
                    "classNumberOfSeats": "200",
                    "classroom": "逸夫楼529",
                    "szlc": ""
                },
                {
                    "classNumberOfSeats": "200",
                    "classroom": "逸夫楼528",
                    "szlc": ""
                },
                {
                    "classNumberOfSeats": "200",
                    "classroom": "逸夫楼523",
                    "szlc": ""
                },
                {
                    "classNumberOfSeats": "200",
                    "classroom": "逸夫楼519",
                    "szlc": ""
                },
                {
                    "classNumberOfSeats": "200",
                    "classroom": "逸夫楼518",
                    "szlc": ""
                },
                {
                    "classNumberOfSeats": "200",
                    "classroom": "逸夫楼517",
                    "szlc": ""
                },
                {
                    "classNumberOfSeats": "200",
                    "classroom": "逸夫楼516",
                    "szlc": ""
                },
                {
                    "classNumberOfSeats": "200",
                    "classroom": "逸夫楼515",
                    "szlc": ""
                },
                {
                    "classNumberOfSeats": "20",
                    "classroom": "药科楼817",
                    "szlc": ""
                },
                {
                    "classNumberOfSeats": "20",
                    "classroom": "药科楼813",
                    "szlc": ""
                },
                {
                    "classNumberOfSeats": "24",
                    "classroom": "药科楼810",
                    "szlc": ""
                },
                {
                    "classNumberOfSeats": "10",
                    "classroom": "药科楼804",
                    "szlc": ""
                },
                {
                    "classNumberOfSeats": "30",
                    "classroom": "药科楼614",
                    "szlc": ""
                },
                {
                    "classNumberOfSeats": "30",
                    "classroom": "药科楼421",
                    "szlc": ""
                },
                {
                    "classNumberOfSeats": "25",
                    "classroom": "药科楼420",
                    "szlc": ""
                },
                {
                    "classNumberOfSeats": "80",
                    "classroom": "药科楼412",
                    "szlc": ""
                },
                {
                    "classNumberOfSeats": "29",
                    "classroom": "药科楼410",
                    "szlc": ""
                },
                {
                    "classNumberOfSeats": "29",
                    "classroom": "药科楼408",
                    "szlc": ""
                },
                {
                    "classNumberOfSeats": "30",
                    "classroom": "药科楼405",
                    "szlc": ""
                },
                {
                    "classNumberOfSeats": "27",
                    "classroom": "药科楼404",
                    "szlc": ""
                },
                {
                    "classNumberOfSeats": "27",
                    "classroom": "药科楼402",
                    "szlc": ""
                },
                {
                    "classNumberOfSeats": "200",
                    "classroom": "药科楼401",
                    "szlc": ""
                },
                {
                    "classNumberOfSeats": "30",
                    "classroom": "药科楼314",
                    "szlc": ""
                },
                {
                    "classNumberOfSeats": "25",
                    "classroom": "药科楼313",
                    "szlc": ""
                },
                {
                    "classNumberOfSeats": "15",
                    "classroom": "药科楼312",
                    "szlc": ""
                },
                {
                    "classNumberOfSeats": "27",
                    "classroom": "药科楼310",
                    "szlc": ""
                },
                {
                    "classNumberOfSeats": "29",
                    "classroom": "药科楼309",
                    "szlc": ""
                },
                {
                    "classNumberOfSeats": "30",
                    "classroom": "药科楼307",
                    "szlc": ""
                },
                {
                    "classNumberOfSeats": "null",
                    "classroom": "药科楼306",
                    "szlc": ""
                },
                {
                    "classNumberOfSeats": "100",
                    "classroom": "药科楼305",
                    "szlc": ""
                },
                {
                    "classNumberOfSeats": "29",
                    "classroom": "药科楼304",
                    "szlc": ""
                },
                {
                    "classNumberOfSeats": "200",
                    "classroom": "药科楼303",
                    "szlc": ""
                },
                {
                    "classNumberOfSeats": "29",
                    "classroom": "药科楼302",
                    "szlc": ""
                },
                {
                    "classNumberOfSeats": "29",
                    "classroom": "药科楼301",
                    "szlc": ""
                },
                {
                    "classNumberOfSeats": "50",
                    "classroom": "药科楼2楼模拟药房",
                    "szlc": ""
                },
                {
                    "classNumberOfSeats": "200",
                    "classroom": "药科楼110",
                    "szlc": ""
                },
                {
                    "classNumberOfSeats": "10",
                    "classroom": "药科大楼506",
                    "szlc": ""
                },
                {
                    "classNumberOfSeats": "10",
                    "classroom": "药科大楼503",
                    "szlc": ""
                },
                {
                    "classNumberOfSeats": "15",
                    "classroom": "药化楼307",
                    "szlc": ""
                },
                {
                    "classNumberOfSeats": "50",
                    "classroom": "卫培三楼",
                    "szlc": ""
                },
                {
                    "classNumberOfSeats": "100",
                    "classroom": "外科实验-1",
                    "szlc": ""
                },
                {
                    "classNumberOfSeats": "100",
                    "classroom": "图书馆四楼",
                    "szlc": ""
                },
                {
                    "classNumberOfSeats": "120",
                    "classroom": "四教010",
                    "szlc": ""
                },
                {
                    "classNumberOfSeats": "100",
                    "classroom": "内科实验-1",
                    "szlc": ""
                },
                {
                    "classNumberOfSeats": "20",
                    "classroom": "六教学楼325",
                    "szlc": ""
                },
                {
                    "classNumberOfSeats": "50",
                    "classroom": "口科B103",
                    "szlc": ""
                },
                {
                    "classNumberOfSeats": "50",
                    "classroom": "口科A203",
                    "szlc": ""
                },
                {
                    "classNumberOfSeats": "200",
                    "classroom": "华西药用植物园",
                    "szlc": ""
                },
                {
                    "classNumberOfSeats": "80",
                    "classroom": "护理学专业",
                    "szlc": ""
                },
                {
                    "classNumberOfSeats": "100",
                    "classroom": "护理实验-1",
                    "szlc": ""
                },
                {
                    "classNumberOfSeats": "100",
                    "classroom": "护理内科-1",
                    "szlc": ""
                },
                {
                    "classNumberOfSeats": "50",
                    "classroom": "公卫新5-2",
                    "szlc": ""
                },
                {
                    "classNumberOfSeats": "50",
                    "classroom": "公卫新5-1",
                    "szlc": ""
                },
                {
                    "classNumberOfSeats": "50",
                    "classroom": "公卫新4-8",
                    "szlc": ""
                },
                {
                    "classNumberOfSeats": "50",
                    "classroom": "公卫新4-2",
                    "szlc": ""
                },
                {
                    "classNumberOfSeats": "50",
                    "classroom": "公卫新4-11",
                    "szlc": ""
                },
                {
                    "classNumberOfSeats": "50",
                    "classroom": "公卫新4-1",
                    "szlc": ""
                },
                {
                    "classNumberOfSeats": "50",
                    "classroom": "公卫新3-5",
                    "szlc": ""
                },
                {
                    "classNumberOfSeats": "50",
                    "classroom": "公卫新3-4",
                    "szlc": ""
                },
                {
                    "classNumberOfSeats": "100",
                    "classroom": "妇产科室-1",
                    "szlc": ""
                },
                {
                    "classNumberOfSeats": "150",
                    "classroom": "法医楼8楼",
                    "szlc": ""
                },
                {
                    "classNumberOfSeats": "50",
                    "classroom": "二教附1号",
                    "szlc": ""
                },
                {
                    "classNumberOfSeats": "100",
                    "classroom": "儿科实验-1",
                    "szlc": ""
                },
                {
                    "classNumberOfSeats": "50",
                    "classroom": "病理学教研",
                    "szlc": ""
                },
                {
                    "classNumberOfSeats": "20",
                    "classroom": "217",
                    "szlc": ""
                }
            ]
        },
        {
            "acmcBuilding": "204",
            "acmcBuildingName": "体育场",
            "claroom": [
                {
                    "classNumberOfSeats": "500",
                    "classroom": "体育馆",
                    "szlc": ""
                },
                {
                    "classNumberOfSeats": "1000",
                    "classroom": "体育场",
                    "szlc": ""
                }
            ]
        },
        {
            "acmcBuilding": "202",
            "acmcBuildingName": "二教",
            "claroom": [
                {
                    "classNumberOfSeats": "60",
                    "classroom": "2-307",
                    "szlc": ""
                },
                {
                    "classNumberOfSeats": "20",
                    "classroom": "2-217",
                    "szlc": ""
                },
                {
                    "classNumberOfSeats": "60",
                    "classroom": "2-212",
                    "szlc": ""
                }
            ]
        },
        {
            "acmcBuilding": "203",
            "acmcBuildingName": "三教",
            "claroom": [
                {
                    "classNumberOfSeats": "60",
                    "classroom": "基础医学专业实验室",
                    "szlc": ""
                },
                {
                    "classNumberOfSeats": "10",
                    "classroom": "3—106",
                    "szlc": ""
                },
                {
                    "classNumberOfSeats": "30",
                    "classroom": "3-312",
                    "szlc": ""
                },
                {
                    "classNumberOfSeats": "30",
                    "classroom": "3-307",
                    "szlc": ""
                },
                {
                    "classNumberOfSeats": "30",
                    "classroom": "3-305",
                    "szlc": ""
                },
                {
                    "classNumberOfSeats": "176",
                    "classroom": "3-117",
                    "szlc": ""
                }
            ]
        },
        {
            "acmcBuilding": "208",
            "acmcBuildingName": "八教",
            "claroom": [
                {
                    "classNumberOfSeats": "300",
                    "classroom": "8-425",
                    "szlc": ""
                },
                {
                    "classNumberOfSeats": "100",
                    "classroom": "8-424",
                    "szlc": ""
                },
                {
                    "classNumberOfSeats": "200",
                    "classroom": "8-334",
                    "szlc": ""
                },
                {
                    "classNumberOfSeats": "15",
                    "classroom": "8-322",
                    "szlc": ""
                },
                {
                    "classNumberOfSeats": "20",
                    "classroom": "8-316",
                    "szlc": ""
                },
                {
                    "classNumberOfSeats": "20",
                    "classroom": "8-315",
                    "szlc": ""
                },
                {
                    "classNumberOfSeats": "160",
                    "classroom": "8-134",
                    "szlc": ""
                },
                {
                    "classNumberOfSeats": "140",
                    "classroom": "8-133",
                    "szlc": ""
                }
            ]
        },
        {
            "acmcBuilding": "209",
            "acmcBuildingName": "九教",
            "claroom": [
                {
                    "classNumberOfSeats": "242",
                    "classroom": "演播厅",
                    "szlc": ""
                },
                {
                    "classNumberOfSeats": "112",
                    "classroom": "4-1",
                    "szlc": ""
                },
                {
                    "classNumberOfSeats": "30",
                    "classroom": "3-4",
                    "szlc": ""
                },
                {
                    "classNumberOfSeats": "30",
                    "classroom": "3-3",
                    "szlc": ""
                },
                {
                    "classNumberOfSeats": "118",
                    "classroom": "3-2",
                    "szlc": ""
                },
                {
                    "classNumberOfSeats": "118",
                    "classroom": "3-1",
                    "szlc": ""
                },
                {
                    "classNumberOfSeats": "51",
                    "classroom": "2-4",
                    "szlc": ""
                },
                {
                    "classNumberOfSeats": "51",
                    "classroom": "2-3",
                    "szlc": ""
                },
                {
                    "classNumberOfSeats": "112",
                    "classroom": "2-2",
                    "szlc": ""
                },
                {
                    "classNumberOfSeats": "112",
                    "classroom": "2-1",
                    "szlc": ""
                },
                {
                    "classNumberOfSeats": "33",
                    "classroom": "1-3",
                    "szlc": ""
                },
                {
                    "classNumberOfSeats": "112",
                    "classroom": "1-2",
                    "szlc": ""
                },
                {
                    "classNumberOfSeats": "112",
                    "classroom": "1-1",
                    "szlc": ""
                }
            ]
        },
        {
            "acmcBuilding": "210",
            "acmcBuildingName": "十教",
            "claroom": [
                {
                    "classNumberOfSeats": "50",
                    "classroom": "四楼",
                    "szlc": ""
                },
                {
                    "classNumberOfSeats": "54",
                    "classroom": "3-4",
                    "szlc": ""
                },
                {
                    "classNumberOfSeats": "114",
                    "classroom": "3-3",
                    "szlc": ""
                },
                {
                    "classNumberOfSeats": "114",
                    "classroom": "3-2",
                    "szlc": ""
                },
                {
                    "classNumberOfSeats": "145",
                    "classroom": "3-1",
                    "szlc": ""
                },
                {
                    "classNumberOfSeats": "54",
                    "classroom": "2-4",
                    "szlc": ""
                },
                {
                    "classNumberOfSeats": "86",
                    "classroom": "2-3",
                    "szlc": ""
                },
                {
                    "classNumberOfSeats": "70",
                    "classroom": "2-2",
                    "szlc": ""
                },
                {
                    "classNumberOfSeats": "68",
                    "classroom": "2-1",
                    "szlc": ""
                },
                {
                    "classNumberOfSeats": "80",
                    "classroom": "1-4",
                    "szlc": ""
                },
                {
                    "classNumberOfSeats": "86",
                    "classroom": "1-3",
                    "szlc": ""
                },
                {
                    "classNumberOfSeats": "200",
                    "classroom": "1-1",
                    "szlc": ""
                }
            ]
        },
        {
            "acmcBuilding": "205",
            "acmcBuildingName": "卫新",
            "claroom": [
                {
                    "classNumberOfSeats": "150",
                    "classroom": "5-2",
                    "szlc": ""
                },
                {
                    "classNumberOfSeats": "150",
                    "classroom": "5-1",
                    "szlc": ""
                },
                {
                    "classNumberOfSeats": "150",
                    "classroom": "4-8",
                    "szlc": ""
                },
                {
                    "classNumberOfSeats": "60",
                    "classroom": "4-6",
                    "szlc": ""
                },
                {
                    "classNumberOfSeats": "60",
                    "classroom": "4-5",
                    "szlc": ""
                },
                {
                    "classNumberOfSeats": "150",
                    "classroom": "4-2",
                    "szlc": ""
                },
                {
                    "classNumberOfSeats": "150",
                    "classroom": "4-11",
                    "szlc": ""
                },
                {
                    "classNumberOfSeats": "150",
                    "classroom": "4-1",
                    "szlc": ""
                },
                {
                    "classNumberOfSeats": "150",
                    "classroom": "3-5",
                    "szlc": ""
                },
                {
                    "classNumberOfSeats": "100",
                    "classroom": "3-4",
                    "szlc": ""
                },
                {
                    "classNumberOfSeats": "60",
                    "classroom": "2-1",
                    "szlc": ""
                },
                {
                    "classNumberOfSeats": "70",
                    "classroom": "1-2",
                    "szlc": ""
                },
                {
                    "classNumberOfSeats": "70",
                    "classroom": "1-1",
                    "szlc": ""
                }
            ]
        },
        {
            "acmcBuilding": "213",
            "acmcBuildingName": "口腔教学楼",
            "claroom": [
                {
                    "classNumberOfSeats": "500",
                    "classroom": "重点实验室",
                    "szlc": ""
                },
                {
                    "classNumberOfSeats": "100",
                    "classroom": "种植实验室",
                    "szlc": ""
                },
                {
                    "classNumberOfSeats": "100",
                    "classroom": "正畸实验室",
                    "szlc": ""
                },
                {
                    "classNumberOfSeats": "100",
                    "classroom": "预防实验室",
                    "szlc": ""
                },
                {
                    "classNumberOfSeats": "100",
                    "classroom": "牙合学实验室",
                    "szlc": ""
                },
                {
                    "classNumberOfSeats": "100",
                    "classroom": "口组病实验室",
                    "szlc": ""
                },
                {
                    "classNumberOfSeats": "100",
                    "classroom": "口修实验室",
                    "szlc": ""
                },
                {
                    "classNumberOfSeats": "100",
                    "classroom": "口外实验室",
                    "szlc": ""
                },
                {
                    "classNumberOfSeats": "100",
                    "classroom": "口生物实验室",
                    "szlc": ""
                },
                {
                    "classNumberOfSeats": "100",
                    "classroom": "口腔制作",
                    "szlc": ""
                },
                {
                    "classNumberOfSeats": "null",
                    "classroom": "口腔医学院",
                    "szlc": ""
                },
                {
                    "classNumberOfSeats": "300",
                    "classroom": "口腔学术厅",
                    "szlc": ""
                },
                {
                    "classNumberOfSeats": "500",
                    "classroom": "口腔临床见习",
                    "szlc": ""
                },
                {
                    "classNumberOfSeats": "100",
                    "classroom": "口内实验室",
                    "szlc": ""
                },
                {
                    "classNumberOfSeats": "100",
                    "classroom": "口解生实验室",
                    "szlc": ""
                },
                {
                    "classNumberOfSeats": "100",
                    "classroom": "放射实验室",
                    "szlc": ""
                },
                {
                    "classNumberOfSeats": "null",
                    "classroom": "仿头模教室",
                    "szlc": ""
                },
                {
                    "classNumberOfSeats": "240",
                    "classroom": "多功能厅",
                    "szlc": ""
                },
                {
                    "classNumberOfSeats": "100",
                    "classroom": "材料实验室",
                    "szlc": ""
                },
                {
                    "classNumberOfSeats": "100",
                    "classroom": "（3）",
                    "szlc": ""
                },
                {
                    "classNumberOfSeats": "90",
                    "classroom": "（2）",
                    "szlc": ""
                },
                {
                    "classNumberOfSeats": "200",
                    "classroom": "（1）",
                    "szlc": ""
                },
                {
                    "classNumberOfSeats": "90",
                    "classroom": "B605",
                    "szlc": ""
                },
                {
                    "classNumberOfSeats": "90",
                    "classroom": "B603",
                    "szlc": ""
                },
                {
                    "classNumberOfSeats": "42",
                    "classroom": "B505",
                    "szlc": ""
                },
                {
                    "classNumberOfSeats": "40",
                    "classroom": "B407",
                    "szlc": ""
                },
                {
                    "classNumberOfSeats": "96",
                    "classroom": "B403",
                    "szlc": ""
                },
                {
                    "classNumberOfSeats": "50",
                    "classroom": "B309",
                    "szlc": ""
                },
                {
                    "classNumberOfSeats": "50",
                    "classroom": "B305",
                    "szlc": ""
                },
                {
                    "classNumberOfSeats": "42",
                    "classroom": "B303",
                    "szlc": ""
                },
                {
                    "classNumberOfSeats": "50",
                    "classroom": "B207",
                    "szlc": ""
                },
                {
                    "classNumberOfSeats": "50",
                    "classroom": "B206",
                    "szlc": ""
                },
                {
                    "classNumberOfSeats": "50",
                    "classroom": "B203",
                    "szlc": ""
                },
                {
                    "classNumberOfSeats": "90",
                    "classroom": "B105",
                    "szlc": ""
                },
                {
                    "classNumberOfSeats": "90",
                    "classroom": "B103",
                    "szlc": ""
                },
                {
                    "classNumberOfSeats": "90",
                    "classroom": "A503",
                    "szlc": ""
                },
                {
                    "classNumberOfSeats": "null",
                    "classroom": "A404",
                    "szlc": ""
                },
                {
                    "classNumberOfSeats": "68",
                    "classroom": "A403",
                    "szlc": ""
                },
                {
                    "classNumberOfSeats": "42",
                    "classroom": "A303",
                    "szlc": ""
                },
                {
                    "classNumberOfSeats": "40",
                    "classroom": "A203",
                    "szlc": ""
                },
                {
                    "classNumberOfSeats": "30",
                    "classroom": "A105",
                    "szlc": ""
                }
            ]
        },
        {
            "acmcBuilding": "206",
            "acmcBuildingName": "卫阶",
            "claroom": [
                {
                    "classNumberOfSeats": "120",
                    "classroom": "1-2",
                    "szlc": ""
                },
                {
                    "classNumberOfSeats": "120",
                    "classroom": "1-1",
                    "szlc": ""
                }
            ]
        },
        {
            "acmcBuilding": "218",
            "acmcBuildingName": "逸夫楼",
            "claroom": [
                {
                    "classNumberOfSeats": "20",
                    "classroom": "三楼生化会议室",
                    "szlc": ""
                },
                {
                    "classNumberOfSeats": "80",
                    "classroom": "基一南",
                    "szlc": ""
                },
                {
                    "classNumberOfSeats": "80",
                    "classroom": "基一北",
                    "szlc": ""
                },
                {
                    "classNumberOfSeats": "20",
                    "classroom": "6楼607",
                    "szlc": ""
                },
                {
                    "classNumberOfSeats": "null",
                    "classroom": "532",
                    "szlc": ""
                },
                {
                    "classNumberOfSeats": "null",
                    "classroom": "530",
                    "szlc": ""
                },
                {
                    "classNumberOfSeats": "null",
                    "classroom": "528",
                    "szlc": ""
                },
                {
                    "classNumberOfSeats": "null",
                    "classroom": "523",
                    "szlc": ""
                }
            ]
        },
        {
            "acmcBuilding": "214",
            "acmcBuildingName": "图书馆",
            "claroom": [
                {
                    "classNumberOfSeats": "120",
                    "classroom": "四楼东教室",
                    "szlc": "4"
                }
            ]
        },
        {
            "acmcBuilding": "216",
            "acmcBuildingName": "五教",
            "claroom": [
                {
                    "classNumberOfSeats": "110",
                    "classroom": "会议室",
                    "szlc": ""
                }
            ]
        },
        {
            "acmcBuilding": "215",
            "acmcBuildingName": "基法学院",
            "claroom": [
                {
                    "classNumberOfSeats": "200",
                    "classroom": "逸夫楼基1北",
                    "szlc": ""
                },
                {
                    "classNumberOfSeats": "160",
                    "classroom": "五教报告厅",
                    "szlc": ""
                }
            ]
        },
        {
            "acmcBuilding": "217",
            "acmcBuildingName": "第三住院大楼",
            "claroom": [
                {
                    "classNumberOfSeats": "200",
                    "classroom": "15楼示教室",
                    "szlc": "15"
                }
            ]
        },
        {
            "acmcBuilding": "250",
            "acmcBuildingName": "虚拟教学楼",
            "claroom": [
                {
                    "classNumberOfSeats": "9999",
                    "classroom": "在线虚拟考场3",
                    "szlc": "1"
                },
                {
                    "classNumberOfSeats": "9999",
                    "classroom": "在线虚拟考场2",
                    "szlc": "1"
                },
                {
                    "classNumberOfSeats": "9999",
                    "classroom": "虚拟在线考试1",
                    "szlc": "1"
                }
            ]
        }
    ],
    "curxqm": "华西"
}

spareroomList = jsonList["spareroomObjList"]

table = Table(
    show_edge=True,
    show_header=True,
    expand=False,
)
table.title = jsonList["curxqm"] + "空闲教室一览表"
table.add_column("[green]教学楼[/]", no_wrap=False, justify="center", style="bold")
table.add_column("[green]教室名+容纳人数[/]", no_wrap=False, justify="center", style="bold")
for obj in spareroomList:
    renderables = []
    for classroom in obj["claroom"]:
        renderables.append(Panel(f"[white bold]{classroom['classroom']}[/]\n[cyan]{classroom['classNumberOfSeats']}[/]", expand=False))
    table.add_row(f"[yellow]{obj['acmcBuilding']}[/] {obj['acmcBuildingName']}", Columns(renderables))

console.print(table)




