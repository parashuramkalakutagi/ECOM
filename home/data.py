


def laptop_details():
    laptop_data = [
        {
            "brand Name": "ThinkPad Yoga",
            "price": "$1033.99",
            "discription": "12.5\" Touch, Core i3-4010U, 4GB, 500GB + 16GB SSD Cache,",
            "reviews": "13 reviews"
        },
        {
            "brand Name": "Pavilion",
            "price": "$609.99",
            "discription": "15.6\", Core i5-4200U, 6GB, 750GB, Windows 8.1",
            "reviews": "4 reviews"
        },
        {
            "brand Name": "Inspiron 15",
            "price": "$745.99",
            "discription": "Moon Silver, 15.6\", Core i7-4510U, 8GB, 1TB, Radeon HD R7 M265 2GB,",
            "reviews": "12 reviews"
        },
        {
            "brand Name": "Dell XPS 13",
            "price": "$1281.99",
            "discription": "13.3\" Touch, Core i5-4210U, 8GB, 128GB SSD, Windows 8.1",
            "reviews": "4 reviews"
        },
        {
            "brand Name": "ThinkPad X230",
            "price": "$1244.99",
            "discription": "12.5\", Core i5 2.6GHz, 8GB, 180GB SSD, Win7 Pro 64bit",
            "reviews": "10 reviews"
        },
        {
            "brand Name": "HP 250 G3",
            "price": "$520.99",
            "discription": "15.6\", Core\u00a0i5-4210U, 4GB, 500GB, Windows 8.1",
            "reviews": "13 reviews"
        },
        {
            "brand Name": "ThinkPad Yoga",
            "price": "$1223.99",
            "discription": "12.5\" Touch, Core i5 4200U, 8GB, 500GB + 16GB SSD Cache, Windows",
            "reviews": "2 reviews"
        },
        {
            "brand Name": "HP 350 G1",
            "price": "$577.99",
            "discription": "15.6\", Core i5-4200U, 4GB, 750GB, Radeon HD8670M 2GB, Windows",
            "reviews": "10 reviews"
        },
        {
            "brand Name": "Asus VivoBook...",
            "price": "$399.00",
            "discription": "Asus VivoBook Max X541NA-GQ041 Black Chocolate, 15.6\" HD, Pentium N4200 1.1GHz, 4GB, 500GB, Windows 10 Home",
            "reviews": "4 reviews"
        },
        {
            "brand Name": "Dell Vostro 15",
            "price": "$488.78",
            "discription": "Dell Vostro 15 (3568) Black, 15.6\" FHD, Core i5-7200U, 4GB, 128GB SSD, Radeon R5 M420 2GB, Linux",
            "reviews": "14 reviews"
        },
        {
            "brand Name": "Acer Spin 5",
            "price": "$564.98",
            "discription": "Acer Spin 5 SP513-51 Black, 13.3\" FHD Touch, Core i3-7100U, 4GB, 128GB SSD, Windows 10 Home",
            "reviews": "0 reviews"
        },
        {
            "brand Name": "Acer Aspire A5...",
            "price": "$679.00",
            "discription": "Acer Aspire A515-51-5654, Black, 15.6\", FHD, Core i5-8250U, 8GB DDR4, 256GB SSD, Windows 10 Home, ENG",
            "reviews": "9 reviews"
        },
        {
            "brand Name": "Dell Inspiron...",
            "price": "$679.00",
            "discription": "Dell Inspiron 15 (5567) Fog Gray, 15.6\" FHD, Core i5-7200U, 8GB, 1TB, Radeon R7 M445 4GB, Linux",
            "reviews": "7 reviews"
        },
        {
            "brand Name": "Asus VivoBook...",
            "price": "$729.00",
            "discription": "Asus VivoBook S14 (S406UA-BV041T) Starry Grey, 14\", Core i5-8250U, 8GB, 256GB SSD, Windows 10 Home, Eng kbd",
            "reviews": "2 reviews"
        },
        {
            "brand Name": "Asus ROG STRIX...",
            "price": "$799.00",
            "discription": "Asus ROG STRIX GL553VD-DM256, 15.6\" FHD, Core i5-7300HQ, 8GB, 1TB, GeForce GTX 1050 2GB, No OS",
            "reviews": "7 reviews"
        },
        {
            "brand Name": "Acer Nitro 5 A...",
            "price": "$809.00",
            "discription": "Acer Nitro 5 AN515-51, 15.6\" FHD IPS, Core i5-7300HQ, 8GB, 1TB, GeForce GTX 1050 2GB, Windows 10 Home",
            "reviews": "0 reviews"
        },
        {
            "brand Name": "Asus ROG STRIX...",
            "price": "$899.00",
            "discription": "Asus ROG STRIX GL553VD-DM256, 15.6\" FHD, Core i5-7300HQ, 8GB, 1TB, GeForce GTX 1050 2GB, No OS + Windows 10 Home",
            "reviews": "7 reviews"
        },
        {
            "brand Name": "Lenovo ThinkPa...",
            "price": "$999.00",
            "discription": "Lenovo ThinkPad L570, 15.6\" FHD, Core i7-7500U, 8GB, 256GB SSD, Windows 10 Pro",
            "reviews": "11 reviews"
        },
        {
            "brand Name": "Lenovo Legion...",
            "price": "$1149.00",
            "discription": "Lenovo Legion Y520-15IKBM, 15.6\" FHD IPS, Core i7-7700HQ, 8GB, 128GB SSD + 1TB, GeForce GTX 1060 Max-Q 6GB, DOS",
            "reviews": "11 reviews"
        },
        {
            "brand Name": "Lenovo Legion...",
            "price": "$1399.00",
            "discription": "Lenovo Legion Y720, 15.6\" FHD IPS, Core i7-7700HQ, 8GB, 128GB SSD + 2TB HDD, GeForce GTX 1060 6GB, DOS, RGB backlit keyboard",
            "reviews": "8 reviews"
        },
        {
            "brand Name": "Asus ROG Strix...",
            "price": "$1769.00",
            "discription": "Asus ROG Strix GL702ZC-GC154T, 17.3\" FHD, Ryzen 7 1700, 16GB, 256GB + 1TB HDD, Radeon RX 580 4GB, Windows 10 Home",
            "reviews": "7 reviews"
        },
        {
            "brand Name": "Asus ROG Strix...",
            "price": "$1769.00",
            "discription": "Asus ROG Strix GL702ZC-GC209T, 17.3\" FHD IPS, Ryzen 7 1700, 16GB, 256GB SSD + 1TB HDD, Radeon RX 580 4GB, Windows 10 Home",
            "reviews": "8 reviews"
        },
        {
            "brand Name": "Asus ROG Strix...",
            "price": "$1799.00",
            "discription": "Asus ROG Strix SCAR Edition GL503VM-ED115T, 15.6\" FHD 120Hz, Core i7-7700HQ, 16GB, 256GB SSD + 1TB SSHD, GeForce GTX 1060 6GB, Windows 10 Home",
            "reviews": "8 reviews"
        },
        {
            "brand Name": "Asus VivoBook...",
            "price": "$295.99",
            "discription": "Asus VivoBook X441NA-GA190 Chocolate Black, 14\", Celeron N3450, 4GB, 128GB SSD, Endless OS, ENG kbd",
            "reviews": "14 reviews"
        },
        {
            "brand Name": "Prestigio Smar...",
            "price": "$299.00",
            "discription": "Prestigio SmartBook 133S Dark Grey, 13.3\" FHD IPS, Celeron N3350 1.1GHz, 4GB, 32GB, Windows 10 Pro + Office 365 1 gadam",
            "reviews": "8 reviews"
        },
        {
            "brand Name": "Prestigio Smar...",
            "price": "$299.00",
            "discription": "Prestigio SmartBook 133S Gold, 13.3\" FHD IPS, Celeron N3350 1.1GHz, 4GB, 32GB, Windows 10 Pro + Office 365 1 gadam",
            "reviews": "12 reviews"
        },
        {
            "brand Name": "Lenovo V110-15...",
            "price": "$321.94",
            "discription": "Lenovo V110-15IAP, 15.6\" HD, Celeron N3350 1.1GHz, 4GB, 128GB SSD, Windows 10 Home",
            "reviews": "5 reviews"
        },
        {
            "brand Name": "Lenovo V110-15...",
            "price": "$356.49",
            "discription": "Asus VivoBook 15 X540NA-GQ008T Chocolate Black, 15.6\" HD, Pentium N4200, 4GB, 500GB, Windows 10 Home, En kbd",
            "reviews": "6 reviews"
        },
        {
            "brand Name": "Hewlett Packar...",
            "price": "$364.46",
            "discription": "Hewlett Packard 250 G6 Dark Ash Silver, 15.6\" HD, Celeron N3060 1.6GHz, 4GB, 128GB SSD, DOS",
            "reviews": "12 reviews"
        },
        {
            "brand Name": "Acer Aspire 3...",
            "price": "$372.70",
            "discription": "Acer Aspire 3 A315-31 Black, 15.6\" HD, Celeron N3350 1.1GHz, 4GB, 128GB SSD, Windows 10 Home",
            "reviews": "2 reviews"
        },
        {
            "brand Name": "Acer Aspire A3...",
            "price": "$379.94",
            "discription": "Acer Aspire A315-31-C33J Black 15.6\", HD, Celeron N3350, 4GB DDR3L, 128GB, Windows 10 Home, ENG",
            "reviews": "0 reviews"
        },
        {
            "brand Name": "Acer Aspire ES...",
            "price": "$379.95",
            "discription": "Acer Aspire ES1-572 Black, 15.6\" HD, Core i3-6006U, 4GB, 128GB SSD, Linux",
            "reviews": "9 reviews"
        },
        {
            "brand Name": "Acer Aspire 3...",
            "price": "$391.48",
            "discription": "Acer Aspire 3 A315-31 Black, 15.6\" HD, Pentium N4200 1.1GHz, 4GB, 128GB SSD, Windows 10 Home",
            "reviews": "10 reviews"
        },
        {
            "brand Name": "Acer Aspire 3...",
            "price": "$393.88",
            "discription": "Acer Aspire 3 A315-21, 15.6\", AMD A4-9120. 4GB. 128GB SSD, Linux",
            "reviews": "9 reviews"
        },
        {
            "brand Name": "Asus VivoBook...",
            "price": "$399.99",
            "discription": "Asus VivoBook E502NA-GO022T Dark Blue, 15.6\" HD, Pentium N4200 1.1GHz, 4GB, 128GB SSD, Windows 10 Home, En/Ru kbd",
            "reviews": "3 reviews"
        },
        {
            "brand Name": "Lenovo ThinkPa...",
            "price": "$404.23",
            "discription": "Lenovo ThinkPad E31-80, 13.3\" HD, Celeron 3855U 1.6GHz, 4GB, 128GB SSD, Windows 10 Home",
            "reviews": "12 reviews"
        },
        {
            "brand Name": "Acer Aspire 3...",
            "price": "$408.98",
            "discription": "Acer Aspire 3 A315-31 Black, 15.6\" HD, Pentium N4200 1.1GHz, 4GB, 128GB SSD, Windows 10 Home",
            "reviews": "10 reviews"
        },
        {
            "brand Name": "Lenovo V110-15...",
            "price": "$409.63",
            "discription": "Lenovo V110-15ISK, 15.6\" HD, Core i3-6006U, 8GB, 128GB SSD, Windows 10 Home",
            "reviews": "9 reviews"
        },
        {
            "brand Name": "Acer Aspire ES...",
            "price": "$410.46",
            "discription": "Acer Aspire ES1-732 Black, 17.3\" HD+, Celeron, N3350, 4GB, 1TB, Windows 10 Home",
            "reviews": "14 reviews"
        },
        {
            "brand Name": "Asus VivoBook...",
            "price": "$410.66",
            "discription": "Asus VivoBook 15 X540NA-GQ026T Chocolate Black, 15.6\" HD, Pentium N4200, 4GB, 128GB SSD, Windows 10 Home, En/Ru kbd",
            "reviews": "4 reviews"
        },
        {
            "brand Name": "Asus EeeBook R...",
            "price": "$433.30",
            "discription": "Asus EeeBook R416NA-FA014T, 14\" FHD, Pentium N4200, 4GB, 128GB eMMC, Windows 10 Home, Eng kbd",
            "reviews": "1 reviews"
        },
        {
            "brand Name": "Acer Aspire 3...",
            "price": "$436.29",
            "discription": "Acer Aspire 3 A315-51, 15.6\" HD, Core i3-6006U, 4GB, 1TB, Windows 10 Home",
            "reviews": "1 reviews"
        },
        {
            "brand Name": "Acer Aspire ES...",
            "price": "$436.29",
            "discription": "Acer Aspire ES1-572 Black, 15.6\" HD, Core i3-6006U, 4GB, 500GB, Windows 10 Home",
            "reviews": "2 reviews"
        },
        {
            "brand Name": "Acer Extensa 1...",
            "price": "$439.73",
            "discription": "Acer Extensa 15 (2540) Black, 15.6\" HD, Core i5-7200U, 4GB, 500GB, Linux",
            "reviews": "6 reviews"
        },
        {
            "brand Name": "Acer Aspire ES...",
            "price": "$454.62",
            "discription": "Acer Aspire ES1-572 Black, 15.6\" HD, Core i5-7200U, 4GB, 500GB, Linux",
            "reviews": "9 reviews"
        },
        {
            "brand Name": "Lenovo V110-15...",
            "price": "$454.73",
            "discription": "Lenovo V110-15ISK, 15.6\" HD, Core i3-6006U, 4GB, 128GB SSD, Windows 10 Pro",
            "reviews": "2 reviews"
        },
        {
            "brand Name": "Acer Aspire A3...",
            "price": "$457.38",
            "discription": "Acer Aspire A315-51-33TG, Black 15.6\" HD, Core i3-7100U, 4GB DDR4, 128GB SSD, Windows 10 Home, ENG",
            "reviews": "9 reviews"
        },
        {
            "brand Name": "Lenovo V110-15...",
            "price": "$465.95",
            "discription": "Lenovo V110-15IKB, 15.6\" HD, Core i5-7200U, 4GB, 500GB, DOS",
            "reviews": "7 reviews"
        },
        {
            "brand Name": "Asus VivoBook...",
            "price": "$468.56",
            "discription": "Asus VivoBook 15 X540UA-DM260 Chocolate Black, 15.6\" FHD, Core i3-6006U, 4GB, 256GB SSD, Endless OS, En kbd",
            "reviews": "1 reviews"
        },
        {
            "brand Name": "Acer Aspire ES...",
            "price": "$469.10",
            "discription": "Acer Aspire ES1-572 Black, 15.6\" HD, Core i3-6006U, 4GB, 128GB SSD, Windows 10 Home",
            "reviews": "5 reviews"
        },
        {
            "brand Name": "Lenovo V510 Bl...",
            "price": "$484.23",
            "discription": "Lenovo V510 Black, 14\" HD, Core i3-6006U, 4GB, 128GB SSD, Windows 10 Home",
            "reviews": "8 reviews"
        },
        {
            "brand Name": "Acer Aspire ES...",
            "price": "$485.90",
            "discription": "Acer Aspire ES1-572 Black, 15.6\" HD, Core i5-7200U, 4GB, 128GB SSD, Linux",
            "reviews": "6 reviews"
        },
        {
            "brand Name": "Lenovo V510 Bl...",
            "price": "$487.80",
            "discription": "Lenovo V510 Black, 15.6\" HD, Core i3-6006U, 4GB, 128GB SSD, Windows 10 Home",
            "reviews": "9 reviews"
        },
        {
            "brand Name": "Acer Swift 1 S...",
            "price": "$488.64",
            "discription": "Acer Swift 1 SF113-31 Silver, 13.3\" FHD, Pentium N4200, 4GB, 128GB SSD, Windows 10 Home",
            "reviews": "4 reviews"
        },
        {
            "brand Name": "Acer Aspire 3...",
            "price": "$494.71",
            "discription": "Acer Aspire 3 A315-51 Black, 15.6\" FHD, Core i3-7100U, 4GB, 500GB + 128GB SSD, Windows 10 Home",
            "reviews": "2 reviews"
        },
        {
            "brand Name": "Dell Vostro 15...",
            "price": "$497.17",
            "discription": "Dell Vostro 15 (3568) Red, 15.6\" HD, Core i5-7200U, 4GB, 1TB, Radeon R5 M420 2GB, Linux",
            "reviews": "9 reviews"
        },
        {
            "brand Name": "Lenovo V510 Bl...",
            "price": "$498.23",
            "discription": "Lenovo V510 Black, 15.6\" FHD, Core i3-7100U, 4GB, 128GB SSD, Windows 10 Pro",
            "reviews": "5 reviews"
        },
        {
            "brand Name": "Lenovo ThinkPa...",
            "price": "$1096.02",
            "discription": "Lenovo ThinkPad L460, 14\" FHD IPS, Core i7-6600U, 8GB, 256GB SSD, Windows 10 Pro",
            "reviews": "14 reviews"
        },
        {
            "brand Name": "Dell Inspiron...",
            "price": "$1098.42",
            "discription": "Dell Inspiron 15 (7567) Black, 15.6\" FHD, Core i5-7300HQ, 8GB, 256GB SSD, GeForce GTX 1050 4GB, Windows 10 Home",
            "reviews": "7 reviews"
        },
        {
            "brand Name": "MSI GL72M 7RDX",
            "price": "$1099.00",
            "discription": "MSI GL72M 7RDX, 17.3\" FHD, Core i5-7300HQ, 8GB, 1TB + 128GB SSD, GeForce GTX 1050 2GB, Windows 10 Home",
            "reviews": "1 reviews"
        },
        {
            "brand Name": "MSI GL72M 7RDX",
            "price": "$1099.00",
            "discription": "Asus ROG Strix GL553VD-DM535T, 15.6\" FHD, Core i7-7700HQ, 8GB, 1TB + 128GB SSD, GeForce GTX 1050 2GB, Windows 10 Home, Eng kbd",
            "reviews": "9 reviews"
        },
        {
            "brand Name": "Asus ROG Strix...",
            "price": "$1101.83",
            "discription": "Apple MacBook Air 13.3\", Core i5 1.8GHz, 8GB, 128GB SSD, Intel HD 4000, RUS",
            "reviews": "4 reviews"
        },
        {
            "brand Name": "Dell Latitude...",
            "price": "$1102.66",
            "discription": "Dell Latitude 5280, 12.5\" HD, Core i5-7300U, 8GB, 256GB SSD, Windows 10 Pro",
            "reviews": "8 reviews"
        },
        {
            "brand Name": "Dell Latitude...",
            "price": "$1110.14",
            "discription": "Dell Latitude 5480, 14\" FHD, Core i5-7300U, 8GB, 500GB, Linux + Windows 10 Home",
            "reviews": "4 reviews"
        },
        {
            "brand Name": "Lenovo Legion...",
            "price": "$1112.91",
            "discription": "Lenovo Legion Y520-15IKBM, Black, 15.6\" FHD IPS, Core i5-7300HQ, 8 GB, 128GB SSD + 2 TB HDD, NVIDIA GeForce GTX 1060 6 GB, FreeDOS + Windows 10 Home",
            "reviews": "1 reviews"
        },
        {
            "brand Name": "Toshiba Porteg...",
            "price": "$1114.55",
            "discription": "Toshiba Portege Z30-C-16J Grey, 13.3\" FHD, Core i5-6200U, 8GB, 256GB SSD, Windows 10 Pro",
            "reviews": "0 reviews"
        },
        {
            "brand Name": "Acer Predator...",
            "price": "$1123.87",
            "discription": "Acer Predator Helios 300 (PH317-51), 17.3\" FHD IPS, Core i5-7300HQ, 8GB, 1TB + 128GB SSD, GeForce GTX 1050Ti 4GB, Windows 10 Home",
            "reviews": "1 reviews"
        },
        {
            "brand Name": "Acer Aspire 7...",
            "price": "$1123.87",
            "discription": "Acer Aspire 7 A715-71G, 15.6\" FHD IPS, Core i7-7700HQ, 8GB, 128GB SSD + 1TB HDD, GTX 1050 Ti 4GB, Windows 10 Home",
            "reviews": "4 reviews"
        },
        {
            "brand Name": "Dell Inspiron...",
            "price": "$1124.20",
            "discription": "Dell Inspiron 17 2in1 (7779) Silver, 17.3\" FHD Touch, Core i5-7200U, 12GB, 1TB, GeForce GT940MX 2GB, Windows 10 Home",
            "reviews": "10 reviews"
        },
        {
            "brand Name": "Dell Latitude...",
            "price": "$1133.82",
            "discription": "Dell Latitude 5480, 14\" FHD, Core i5-7300U, 8GB, 500GB, Windows 10 Pro",
            "reviews": "14 reviews"
        },
        {
            "brand Name": "Lenovo Legion...",
            "price": "$1133.91",
            "discription": "Lenovo Legion Y520, 15.6\" FHD, Core i7-7700HQ, 8GB, 128 GB SSD + 1TB HDD, GTX 1050 4GB, Windows 10 Home",
            "reviews": "13 reviews"
        },
        {
            "brand Name": "Asus AsusPro A...",
            "price": "$1139.54",
            "discription": "Asus AsusPro Advanced BU401LA-FA271G Dark Grey, 14\", Core i5-4210U, 4GB, 128GB SSD, Win7 Pro 64bit, ENG",
            "reviews": "7 reviews"
        },
        {
            "brand Name": "Acer Nitro 5 A...",
            "price": "$1140.62",
            "discription": "Acer Nitro 5 AN515-51, 15.6\" FHD IPS, Core i7-7700HQ, 8GB, 256GB SSD +1TB, GeForce GTX 1050 Ti 4GB, Windows 10 Home + Windows 10 Home",
            "reviews": "14 reviews"
        },
        {
            "brand Name": "Dell Latitude...",
            "price": "$1143.40",
            "discription": "Dell Latitude 5480, 14\" FHD, Core i5-7440HQ, 8GB, 256GB SSD, Windows 10 Pro",
            "reviews": "5 reviews"
        },
        {
            "brand Name": "Dell Inspiron...",
            "price": "$1144.20",
            "discription": "Dell Inspiron 15 (7567) Black, 15.6\" FHD, Core i7-7700HQ, 8GB, 1TB, GeForce GTX 1050 Ti 4GB, Linux + Windows 10 Home",
            "reviews": "2 reviews"
        },
        {
            "brand Name": "Dell Latitude...",
            "price": "$1144.40",
            "discription": "Dell Latitude 5580, 15.6\" FHD, Core i5-7300U, 8GB, 256GB SSD, Windows 10 Pro",
            "reviews": "10 reviews"
        },
        {
            "brand Name": "MSI GP62M 7RDX...",
            "price": "$1149.00",
            "discription": "MSI GP62M 7RDX Leopard, 15.6\" FHD, Core i7-7700HQ, 8GB, 1TB + 128GB SSD, GeForce GTX 1050 2GB, Windows 10 Home",
            "reviews": "11 reviews"
        },
        {
            "brand Name": "Lenovo Yoga 72...",
            "price": "$1149.73",
            "discription": "Lenovo Yoga 720 Grey, 15.6\" FHD IPS, Core i5-7300HQ, 8GB, 256GB SSD, GeForce GTX 1050 2GB, Windows 10 Home",
            "reviews": "12 reviews"
        },
        {
            "brand Name": "Toshiba Porteg...",
            "price": "$1154.04",
            "discription": "Toshiba Portege Z30-C-16L Grey, 13.3\" FHD, Core i7-6500U, 8GB, 256GB SSD, Windows 10 Pro",
            "reviews": "7 reviews"
        },
        {
            "brand Name": "Acer TravelMat...",
            "price": "$1170.10",
            "discription": "Acer TravelMate P645-S-511A Black, 14\" FHD IPS, Core i5-5200U, 8GB, 256GB SSD, 3G, Windows 10 Pro",
            "reviews": "0 reviews"
        },
        {
            "brand Name": "Dell Latitude...",
            "price": "$1178.19",
            "discription": "Dell Latitude 5580, 15.6\" FHD, Core i5-7300U, 16GB, 256GB SSD, Linux + Windows 10 Home",
            "reviews": "6 reviews"
        },
        {
            "brand Name": "MSI GS63 7RD S...",
            "price": "$1179.00",
            "discription": "MSI GS63 7RD Stealth, 15.6\" FHD IPS, Core i7-7700HQ, 8GB, 256GB SSD, GeForce GTX 1050 2GB, DOS + Windows 10 Home",
            "reviews": "2 reviews"
        },
        {
            "brand Name": "Dell Latitude...",
            "price": "$1187.88",
            "discription": "Dell Latitude 5480, 14\" FHD, Core i5-7300U, 8GB, 256GB SSD, Windows 10 Pro",
            "reviews": "5 reviews"
        },
        {
            "brand Name": "Acer Predator...",
            "price": "$1187.98",
            "discription": "Acer Predator Helios 300 (PH317-51), 17.3\" FHD IPS, Core i7-7700HQ. 8GB, 128GB SSD +1TB, GeForce GTX 1050Ti 4GB, Linux + Windows 10 Home",
            "reviews": "14 reviews"
        },
        {
            "brand Name": "MSI GL62M 7REX",
            "price": "$1199.00",
            "discription": "MSI GL62M 7REX, 15.6\" FHD, Core i7-7700HQ, 8GB, 1TB + 128GB SSD, GeForce GTX 1050 Ti 2GB, Windows 10 Home",
            "reviews": "7 reviews"
        },
        {
            "brand Name": "MSI GL62M 7REX...",
            "price": "$1199.00",
            "discription": "MSI GL62M 7REX2, 15.6\" FHD, Core i7-7700HQ, 8GB, 1TB + 128GB SSD, GeForce GTX 1050 Ti 2GB, Windows 10 Home",
            "reviews": "12 reviews"
        },
        {
            "brand Name": "Lenovo Yoga 91...",
            "price": "$1199.73",
            "discription": "Lenovo Yoga 910 Grey, 13.9\" FHD Touch, Core i5-7200U, 8GB, 256GB SSD, Windows 10 Home",
            "reviews": "7 reviews"
        },
        {
            "brand Name": "Toshiba Porteg...",
            "price": "$1203.41",
            "discription": "Toshiba Portege X30-D-10J Black/Blue, 13.3\" FHD IPS, Core i5-7200U, 8GB, 256GB SSD, Windows 10 Pro",
            "reviews": "13 reviews"
        },
        {
            "brand Name": "Lenovo IdeaPad...",
            "price": "$1212.16",
            "discription": "Lenovo IdeaPad Miix 510 Platinum Silver, 12.2\" IPS Touch, Core i5-7200U, 8GB, 256GB SSD, 4G, Windows 10 Pro",
            "reviews": "0 reviews"
        },
        {
            "brand Name": "Acer Predator...",
            "price": "$1221.58",
            "discription": "Acer Predator Helios 300 (PH317-51), 17.3\" FHD IPS, Core i7-7700HQ, 8GB, 1TB + 128GB SSD, GeForce GTX 1050 Ti 4GB, Windows 10 Home",
            "reviews": "9 reviews"
        },
        {
            "brand Name": "Asus VivoBook...",
            "price": "$1235.49",
            "discription": "Asus VivoBook Pro 15 N580VN-FI006T Gold Metal, 15.6\" UHD, Core i7-7700HQ, 16GB, 1TB + 256GB SSD, GeForce MX150 2GB, Windows 10 Home, Eng kbd",
            "reviews": "10 reviews"
        },
        {
            "brand Name": "Dell Latitude...",
            "price": "$1238.37",
            "discription": "Dell Latitude 5480, 14\" FHD, Core i7-7600U, 8GB, 256GB SSD, Linux",
            "reviews": "0 reviews"
        },
        {
            "brand Name": "Asus ZenBook U...",
            "price": "$1239.20",
            "discription": "Asus ZenBook UX530UX-FY040T Blue, 15.6\" FHD, Core i7-7500U, 8GB, 512GB SSD, GeForce GTX950M 2GB, Windows 10 Home, Eng kbd",
            "reviews": "14 reviews"
        },
        {
            "brand Name": "Asus ROG Strix...",
            "price": "$1259.00",
            "discription": "Asus ROG Strix GL753VE-GC096T, 17.3\" FHD, Core i7-7700HQ, 8GB, 1TB + 128GB SSD, GeForce GTX 1050 Ti 4GB, Windows 10 Home, Eng kbd",
            "reviews": "7 reviews"
        },
        {
            "brand Name": "Apple MacBook...",
            "price": "$1260.13",
            "discription": "Apple MacBook Air 13\", i5 1.8GHz, 8GB, 256GB SSD, Intel HD 6000, ENG",
            "reviews": "8 reviews"
        },
        {
            "brand Name": "Dell Latitude...",
            "price": "$1271.06",
            "discription": "Dell Latitude 5480, 14\" FHD, Core i7-7600U, 8GB, 1TB, GeForce GT930MX, Windows 10 Pro",
            "reviews": "13 reviews"
        },
        {
            "brand Name": "Hewlett Packar...",
            "price": "$1273.11",
            "discription": "Hewlett Packard Spectre 13-v106na Dark Ash Silver, 13.3\" FHD IPS, Core i5-7200U, 8GB, 256GB SSD, Windows 10 Home",
            "reviews": "8 reviews"
        },
        {
            "brand Name": "Toshiba Porteg...",
            "price": "$1294.74",
            "discription": "Toshiba Portege Z30-C-16K Grey, 13.3\" FHD, Core i5-6200U, 8GB, 256GB SSD, 4G, Windows 10 Pro",
            "reviews": "6 reviews"
        },
        {
            "brand Name": "MSI GL62VR 7RF...",
            "price": "$1299.00",
            "discription": "MSI GL62VR 7RFX, 15.6\" FHD, Core i7-7700HQ, 8GB, 1TB + 256GB SSD, GeForce GTX 1060 3GB, Windows 10 Home",
            "reviews": "1 reviews"
        },
        {
            "brand Name": "Dell Latitude...",
            "price": "$1310.39",
            "discription": "Dell Latitude 5480, 14\" FHD, Core i7-7600U, 8GB, 256GB SSD, Windows 10 Pro",
            "reviews": "8 reviews"
        },
        {
            "brand Name": "Hewlett Packar...",
            "price": "$1326.83",
            "discription": "Hewlett Packard ProBook 640 G3, 14\" FHD, Core i7-7600U, 8GB, 256GB SSD, Windows 10 Pro",
            "reviews": "2 reviews"
        },
        {
            "brand Name": "Apple MacBook...",
            "price": "$1333.00",
            "discription": "Apple MacBook Pro 13\" Space Gray, Core i5 2.3GHz, 8GB, 128GB SSD, Iris Plus 640, ENG",
            "reviews": "0 reviews"
        },
        {
            "brand Name": "Dell Latitude...",
            "price": "$1337.28",
            "discription": "Dell Latitude 5580, 15.6\" FHD, Core i7-7600U, 8GB, 256GB SSD, GeForce GT930MX, Windows 10 Pro",
            "reviews": "6 reviews"
        },
        {
            "brand Name": "Dell Latitude...",
            "price": "$1338.37",
            "discription": "Dell Latitude 5480, 14\" FHD, Core i7-7600U, 8GB, 256GB SSD, Linux + Windows 10 Home",
            "reviews": "11 reviews"
        },
        {
            "brand Name": "Dell Latitude...",
            "price": "$1341.22",
            "discription": "Dell Latitude 5580, 15.6\" FHD, Core i7-7600U, 16GB, 256GB SSD, GeForce GT930MX, Linux",
            "reviews": "3 reviews"
        },
        {
            "brand Name": "Apple MacBook...",
            "price": "$1347.78",
            "discription": "Apple MacBook Air 13\", Intel Core i5 1.8GHz, 8GB, 256GB SSD, Intel HD 6000, RUS",
            "reviews": "11 reviews"
        },
        {
            "brand Name": "Lenovo ThinkPa...",
            "price": "$1349.23",
            "discription": "Lenovo ThinkPad T470, 14\" FHD IPS, Core i5-7200U, 8GB, 256GB SSD, Windows 10 Pro",
            "reviews": "5 reviews"
        },
        {
            "brand Name": "Lenovo ThinkPa...",
            "price": "$1362.24",
            "discription": "Lenovo ThinkPad Yoga 370 Black, 13.3\" FHD IPS Touch, Core i5-7200U, 8GB, 256GB SSD, 4G, Windows 10 Pro",
            "reviews": "12 reviews"
        },
        {
            "brand Name": "Toshiba Porteg...",
            "price": "$1366.32",
            "discription": "Toshiba Portege X20W-D-10V Black/Blue, 12.5\" FHD Touch, Core i7-7500U, 8GB, 512GB SSD, Windows 10 Pro",
            "reviews": "11 reviews"
        },
        {
            "brand Name": "Asus ASUSPRO B...",
            "price": "$1381.13",
            "discription": "Asus ASUSPRO B9440UA-GV0279R Gray, 14\" FHD, Core i7-7500U, 16GB, 512GB SSD, Windows 10 Pro, Eng kbd",
            "reviews": "4 reviews"
        },
        {
            "brand Name": "Asus ROG Strix...",
            "price": "$1399.00",
            "discription": "Asus ROG Strix GL702VM-GC146T, 17.3\" FHD, Core i7-7700HQ, 8GB, 1TB + 128GB SSD, GeForce GTX 1060 3GB, Windows 10 Home, Eng kbd",
            "reviews": "10 reviews"
        }
    ]
    return laptop_data


def One_plus_data():
    one_plus = [
        {
            "Product_Name": "OnePlus 11 5G (Titan Black, 16GB RAM, 256GB Storage)",
            "Product_Price": "61,999",
            "Product_Reviews": "4,259"
        },
        {
            "Product_Name": "OnePlus 10T 5G (Jade Green, 8GB RAM, 128GB Storage)",
            "Product_Price": "39,999",
            "Product_Reviews": "4,390"
        },
        {
            "Product_Name": "OnePlus 10T 5G (Moonstone Black, 12GB RAM, 256GB Storage)",
            "Product_Price": "44,999",
            "Product_Reviews": "4,390"
        },
        {
            "Product_Name": "OnePlus Nord CE 2 5G (Bahamas Blue, 8GB RAM, 128GB Storage)",
            "Product_Price": "24,999",
            "Product_Reviews": "137,732"
        },
        {
            "Product_Name": "OnePlus 10 Pro 5G (Emerald Forest, 8GB RAM, 128GB Storage)",
            "Product_Price": "52,999",
            "Product_Reviews": "6,289"
        },
        {
            "Product_Name": "OnePlus 10 Pro 5G (Volcanic Black, 8GB RAM, 128GB Storage)",
            "Product_Price": "52,999",
            "Product_Reviews": "6,289"
        },
        {
            "Product_Name": "(Renewed) OnePlus 6 (Mirror Black, 6GB RAM, 64GB Storage)",
            "Product_Price": "11,999",
            "Product_Reviews": "457"
        },
        {
            "Product_Name": "(Refurbished) OnePlus 5T (Midnight Black, 6GB RAM, 64GB Storage)",
            "Product_Price": "9,190",
            "Product_Reviews": "708"
        },
        {
            "Product_Name": "(Renewed) OnePlus 5T (Midnight Black, 128GB)",
            "Product_Price": "",
            "Product_Reviews": "708"
        },
        {
            "Product_Name": "OnePlus Nord CE 3 Lite 5G (Chromatic Gray, 8GB RAM, 128GB Storage)",
            "Product_Price": "19,999",
            "Product_Reviews": "30,644"
        },
        {
            "Product_Name": "OnePlus Nord CE 3 Lite 5G (Pastel Lime, 8GB RAM, 128GB Storage)",
            "Product_Price": "19,999",
            "Product_Reviews": "30,644"
        },
        {
            "Product_Name": "OnePlus Nord CE 3 Lite 5G (Chromatic Gray, 8GB RAM, 256GB Storage)",
            "Product_Price": "21,999",
            "Product_Reviews": "30,644"
        },
        {
            "Product_Name": "OnePlus Nord CE 3 5G (Aqua Surge, 8GB RAM, 128GB Storage)",
            "Product_Price": "26,998",
            "Product_Reviews": "3,426"
        },
        {
            "Product_Name": "OnePlus Nord CE 3 5G (Aqua Surge, 12GB RAM, 256GB Storage)",
            "Product_Price": "28,998",
            "Product_Reviews": "3,426"
        },
        {
            "Product_Name": "OnePlus Nord CE 3 Lite 5G (Pastel Lime, 8GB RAM, 256GB Storage)",
            "Product_Price": "21,998",
            "Product_Reviews": "30,644"
        },
        {
            "Product_Name": "Oneplus Nord CE 3 5G (Grey Shimmer, 8GB RAM, 128GB Storage)",
            "Product_Price": "26,999",
            "Product_Reviews": "3,426"
        },
        {
            "Product_Name": "OnePlus Nord CE 3 5G (Grey Shimmer, 12GB RAM, 256GB Storage)",
            "Product_Price": "28,999",
            "Product_Reviews": "3,426"
        },
        {
            "Product_Name": "OnePlus Nord 3 5G (Misty Green, 8GB RAM, 128GB Storage)",
            "Product_Price": "33,999",
            "Product_Reviews": "2,067"
        },
        {
            "Product_Name": "OnePlus 11R 5G (Galactic Silver, 8GB RAM, 128GB Storage)",
            "Product_Price": "39,999",
            "Product_Reviews": "9,076"
        },
        {
            "Product_Name": "OnePlus 10R 5G (Forest Green, 8GB RAM, 128GB Storage, 80W SuperVOOC)",
            "Product_Price": "27,999",
            "Product_Reviews": "17,564"
        },
        {
            "Product_Name": "OnePlus 10R 5G (Sierra Black, 8GB RAM, 128GB Storage, 80W SuperVOOC)",
            "Product_Price": "27,999",
            "Product_Reviews": "17,564"
        }
    ]
    return one_plus