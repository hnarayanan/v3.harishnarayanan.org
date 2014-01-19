#!/usr/bin/python

import random

numberneeded = 29;
outputfile = 'image-gallery.html';

imagedata = [
('01_Blue Tranquility.jpg', 'Blue Tranquility'),
('02_Honey Factory Drone.jpg', 'Honey Factory Drone'),
('03_Mississippian Sunset.jpg', 'Mississippian Sunset'), 
('04_Death.jpg', 'Death'),
('05_Lampost Inverse.jpg', 'Lampost Inverse'),
('06_Fastlane.jpg', 'Fastlane'),		     
('07_Bug\'s Eye View.jpg', 'Bug&#8217;s Eye View'),	     
('08_Bostonian Harbour.jpg', 'Bostonian Harbour'),     
('09_Overworked Slave.jpg', 'Overworked Slave'),
('10_Leaky Faucet.jpg', 'Leaky Faucet'),
('11_Instant Stalactites.jpg', 'Instant Stalactites'),
('12_Sunny Scotland.jpg', 'Sunny Scotland'),
('13_True Fans.jpg', 'True Fans'),
('14_Optical Fibre.jpg', 'Optical Fibre'),
('15_Rippled Quadrants.jpg', 'Rippled Quadrants'),
('16_Scientists\' Tools.jpg', 'Scientists&#8217; Tools'),
('17_Light Stream.jpg', 'Light Stream'),
('18_Naturally Desaturated.jpg', 'Naturally Desaturated'),
('19_Icebox Art.jpg', 'Icebox Art'),
('20_Anchor\'s End.jpg', 'Anchor&#8217;s End'),
('21_Virginal.jpg', 'Virginal'),
('22_Age of Innocence.jpg', 'Age of Innocence'),
('23_Nascent Love.jpg', 'Nascent Love'),
('24_Nailed Rails.jpg', 'Nailed Rails'),
('25_Timidly Linear.jpg', 'Timidly Linear'),
('26_Scottish Highlands.jpg', 'Scottish Highlands'),
('27_Paid Vacation.jpg', 'Paid Vacation'),
('28_Freedom of Speech.jpg', 'Freedom of Speech'),
('29_Circle of Life.jpg', 'Circle of Life'),
];

possibilities = range (0,len(imagedata),1);
chosen = random.sample(possibilities,numberneeded);

galleryfile = open (outputfile,'w');

for imagenumber in chosen:
    galleryfile.write('		    <a href="images/photos/'+imagedata[imagenumber][0]+'" rel="lightbox[gallery]" title="'+imagedata[imagenumber][1]+'"><img class="thumbnail-photo" src="images/photos/thumbnails/'+imagedata[imagenumber][0]+'" alt="'+imagedata[imagenumber][1]+'" /></a>\n');

galleryfile.close();
