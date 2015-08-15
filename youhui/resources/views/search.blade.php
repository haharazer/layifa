@extends('layout')

@section('content')
    <link rel="stylesheet" href="{{asset('/css/home.css')}}">

    <script>
        function showImg( url ) {
            var imgid = Math.random(), frameid = 'frameimg' + imgid;
            window['img'+imgid] = '<img id="img" width="200px" height="200px" src=\''+url+'?kilobug\' /><script>window.onload = function() { parent.document.getElementById(\''+frameid+'\').height = document.getElementById(\'img\').height+\'px\'; }<'+'/script>';
            document.write('<iframe id="'+frameid+'" src="javascript:parent[\'img'+imgid+'\'];" frameBorder="0" scrolling="no" width="100%"></iframe>');
        }
    </script>

    <div class="col-md-12">
        <div class="row">
            @foreach ($items as $item)
                <div class="col-sm-6 col-md-4">
                    <div class="thumbnail" style="height: 470px">
                        <div class="goods">
                            <script>
                                showImg("{{ $item->img }}");
                            </script>
                            <div class="caption">
                                <h2 class="itemName">
                                    <a href="{{ $item->url }}" target="_blank">
                                        <span class="black">{{ $item->title }}</span>
                                        <span class="red">{{ $item->price }}</span>
                                    </a>
                                </h2>
                                <div class="timeInfo">
                                    <span class="time">{{ date('m-d H:i', $item->timestamp) }}</span>
                                </div>
                                <p class="itemContent">{!! $item->content !!}</p>
                                <div class="buy">
                                    <a href="{{ $item->link }}" class="link" target="_blank">原始链接</a>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            @endforeach
        </div>

        <nav>
            <ul class="pager">
            @if($page == 1)
                <li class="previous disabled"><a href="#"><span aria-hidden="true">&larr;</span> Older</a></li>
            @else
                <li class="previous"><a href="{{ route('search', ['page' => $page - 1, 'query' => $query]) }}"><span aria-hidden="true">&larr;</span> Older</a></li>
            @endif
            <li class="next"><a href="{{ route('search', ['page' => $page + 1, 'query' => $query]) }}">Newer <span aria-hidden="true">&rarr;</span></a></li>
            </ul>
        </nav>
    </div>
@endsection
