define(['backbone', 'underscore', 'jquery', 'ol', 'olMapboxStyle'], function (Backbone, _, $, ol, OlMapboxStyle) {
    return Backbone.View.extend({
        getVectorTileMapBoxStyle: function (url, styleUrl, layerName, attributions) {
            var tilegrid = ol.tilegrid.createXYZ({tileSize: 512, maxZoom: 14});
            var layer = new ol.layer.VectorTile({
                source: new ol.source.VectorTile({
                    attributions: attributions,
                    format: new ol.format.MVT(),
                    tileGrid: tilegrid,
                    tilePixelRatio: 8,
                    url: url
                })
            });
            fetch(styleUrl).then(function (response) {
                response.json().then(function (glStyle) {
                    OlMapboxStyle.applyStyle(layer, glStyle, layerName).then(function () {
                    });
                });
            });
            return layer
        },
        getOpenMapTilesTile: function (styleUrl) {
            var attributions = '© <a href="https://openmaptiles.org/">OpenMapTiles</a> ' +
                '© <a href="http://www.openstreetmap.org/copyright">' +
                'OpenStreetMap contributors</a>';
            return this.getVectorTileMapBoxStyle(
                'https://maps.tilehosting.com/data/v3/{z}/{x}/{y}.pbf.pict?key=' + mapTilerKey,
                styleUrl,
                'openmaptiles',
                attributions
            );
        },
        getKlokantechTerrainBasemap: function () {
            var attributions = '© <a href="https://openmaptiles.org/">OpenMapTiles</a> ' +
                '© <a href="http://www.openstreetmap.org/copyright">' +
                'OpenStreetMap contributors</a>';
            var openMapTiles = this.getOpenMapTilesTile(staticURL + 'mapbox-style/klokantech-terrain-gl-style.json');
            var contours = this.getVectorTileMapBoxStyle(
                'https://maps.tilehosting.com/data/contours/{z}/{x}/{y}.pbf.pict?key=' + mapTilerKey,
                staticURL + 'mapbox-style/klokantech-terrain-gl-style.json',
                'contours',
                attributions
            );
            var hillshading = new ol.layer.Tile({
                opacity: 0.1,
                source: new ol.source.XYZ({
                    url: 'https://maps.tilehosting.com/data/hillshades/{z}/{x}/{y}.png?key=' + mapTilerKey
                })
            });
            return new ol.layer.Group({
                title: 'Klokantech Terrain',
                layers: [openMapTiles, hillshading, contours]
            });
        },
        getPositronBasemap: function () {
            var layer = this.getOpenMapTilesTile(
                staticURL + 'mapbox-style/positron-gl-style.json');
            layer.set('title', 'Positron Map');
            return layer
        },
        getDarkMatterBasemap: function () {
            var layer = this.getOpenMapTilesTile(
                staticURL + 'mapbox-style/dark-matter-gl-style.json');
            layer.set('title', 'Dark Matter');
            return layer
        }
    })
});
