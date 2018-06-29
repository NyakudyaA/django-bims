define(['backbone', 'underscore', 'jquery', 'ol'], function (Backbone, _, $, ol) {
    return Backbone.View.extend({
        styles: {
            'Point': new ol.style.Style({
                image: new ol.style.Icon(/** @type {olx.style.IconOptions} */ ({
                    anchor: [0.5, 46],
                    anchorXUnits: 'fraction',
                    anchorYUnits: 'pixels',
                    opacity: 0.75,
                    src: '/static/img/map-marker.png'
                })),
                text: new ol.style.Text({
                    scale: 1,
                    fill: new ol.style.Fill({
                        color: '#000000'
                    })
                })
            }),
            'LineString': new ol.style.Style({
                stroke: new ol.style.Stroke({
                    color: 'green',
                    width: 1
                })
            }),
            'MultiPolygon': new ol.style.Style({
                stroke: new ol.style.Stroke({
                    color: 'yellow',
                    width: 1
                }),
                fill: new ol.style.Fill({
                    color: 'rgba(255, 255, 0, 0.1)'
                })
            }),
            'Polygon': new ol.style.Style({
                stroke: new ol.style.Stroke({
                    color: 'blue',
                    lineDash: [4],
                    width: 3
                }),
                fill: new ol.style.Fill({
                    color: 'rgba(0, 0, 255, 0.1)'
                })
            })
        },
        getSiteStyle: function (type) {
            return this.styles[type]
        },
        getClusterStyle: function (count) {
            var smallCluster = new ol.style.Circle({
                radius: 15,
                fill: new ol.style.Fill({
                    color: 'red'
                })
            });
            var mediumCluster = new ol.style.Circle({
                radius: 30,
                fill: new ol.style.Fill({
                    color: 'yellow'
                })
            });
            var largeCluster = new ol.style.Circle({
                radius: 45,
                fill: new ol.style.Fill({
                    color: 'green'
                })
            });
            var image = null;
            if (count < 10) {
                image = smallCluster;
            } else if (10 >= count <= 100) {
                image = mediumCluster;
            } else {
                image = largeCluster
            }
            return new ol.style.Style({
                image: image,
                text: new ol.style.Text({
                    scale: 1,
                    fill: new ol.style.Fill({
                        color: '#000000'
                    })
                })
            });
        },
        getHighlightStyle: function (geometryType) {
            var style;
            if (geometryType != 'Point') {
                style = new ol.style.Style({
                    stroke: new ol.style.Stroke({
                        color: [255, 0, 0, 0.8],
                        width: 2
                    }),
                    fill: new ol.style.Fill({
                        color: [255, 0, 0, 0.8]
                    })
                })
            } else {
                style = new ol.style.Style({
                    image: new ol.style.Icon(({
                        anchor: [0.5, 46],
                        anchorXUnits: 'fraction',
                        anchorYUnits: 'pixels',
                        opacity: 0.75,
                        src: '/static/img/map-marker-highlight.png'
                    })),
                    text: new ol.style.Text({
                        scale: 1,
                        fill: new ol.style.Fill({
                            color: '#000000'
                        })
                    })
                })
            }
            return style;
        },
    })
});